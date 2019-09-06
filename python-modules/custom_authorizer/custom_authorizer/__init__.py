import logging
import json
import boto3
import os

REGION = os.getenv('REGION', 'us-west-2')
ssm = boto3.client('ssm', region_name=REGION)
SERVICE = os.getenv('SERVICE')
STAGE = os.getenv('STAGE')
RESOURCE_NAME = os.getenv('RESOURCE_NAME')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Authorizer(object):

    def __init__(self, service=SERVICE, stage=STAGE, resource=RESOURCE_NAME):
        self.service = service
        self.stage = stage
        self.resource = resource

    def generate_policy(self, principalId, effect, resource):
        authResponse = {}
        authResponse['principalId'] = principalId
        if effect and resource:
            policyDocument = {}
            policyDocument['Version'] = '2012-10-17'
            policyDocument['Statement'] = []
            statementOne = {}
            statementOne['Action'] = 'execute-api:Invoke'
            statementOne['Effect'] = effect
            statementOne['Resource'] = resource
            policyDocument['Statement'].append(statementOne)
            authResponse['policyDocument'] = policyDocument

        return authResponse

    def get_token(self):
        try:
            logger.info("Obtaining auth token from SSM.")
            response = ssm.get_parameter(
                Name="/{}/{}/{}/auth_token".format(self.service, self.stage, self.resource),
                WithDecryption=True
            )
            token = response['Parameter']['Value']
            return token
        except Exception as e:
            logger.error("A problem occurred while accessing SSM, exception: {}".format(e))
            return False
    
    # Need to make this function generic
    def authorize(self, event, context):
        # print(json.dumps(event))
        if 'authorizationToken' not in event:
            logger.error("No authorization header received, denying access.")
            return {
                'statusCode': 403,
                'body': json.dumps('Unauthorized.')
            }
        else:
            token = event['authorizationToken']
            ssm_zoom_token = self.get_token()
            if not ssm_zoom_token:
                # Unable to fetch Zoom token from SSM for some reason, return "Deny"
                logger.error("Unable to retrieve Zoom token from SSM.")
                deny_response = self.generate_policy('zoom_webhook', 'Deny', event['methodArn'])
            elif ssm_zoom_token and str(token) == ssm_zoom_token:
                # Correct authorization token, we should allow
                logger.info("Correct authorization token received, passing event to handler.")
                allow_response = self.generate_policy('zoom_webhook', 'Allow', event['methodArn'])
                return allow_response
            else:
                # Incorrect token received, we should deny
                # TODO: We should implement monitoring on "Deny" events
                # This will be done in another PR
                logger.warning("Incorrect authorization token received, dropping event.")
                deny_response = self.generate_policy('zoom_webhook', 'Deny', event['methodArn'])
                return deny_response

        # Default response
        return {
            'statusCode': 403,
            'body': json.dumps('Unauthorized.')
        }
