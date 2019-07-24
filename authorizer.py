import logging
import json
import boto3
import os

REGION = os.getenv('REGION', 'us-west-2')
ssm = boto3.client('ssm', region_name=REGION)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def generate_policy(principalId, effect, resource):
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


def get_zoom_token():
    try:
        logger.info("Obtaining Zoom auth token from SSM.")
        response = ssm.get_parameter(Name="/mozdef-event-framework/ZOOM_AUTH_TOKEN", WithDecryption=True)
        zoom_token = response['Parameter']['Value']
        return zoom_token
    except Exception as e:
        logger.error("A problem occurred while accessing SSM, exception: {}".format(e))
        return False


def validate_token(event, context):
    # print(json.dumps(event))

    if 'authorizationToken' not in event:
        logger.error("No authorization header received, denying access.")
        return {
            'statusCode': 403,
            'body': json.dumps('Unauthorized.')
        }
    else:
        token = event['authorizationToken']
        ssm_zoom_token = get_zoom_token()
        if not ssm_zoom_token:
            # Unable to fetch Zoom token from SSM for some reason, return "Deny"
            logger.error("Unable to retrieve Zoom token from SSM.")
            deny_response = generate_policy('zoom_webhook', 'Deny', event['methodArn'])
        elif ssm_zoom_token and str(token) == ssm_zoom_token:
            # Correct authorization token, we should allow
            logger.info("Correct authorization token received, passing event to handler.")
            allow_response = generate_policy('zoom_webhook', 'Allow', event['methodArn'])
            return allow_response
        else:
            # Incorrect token received, we should deny
            # TODO: We should implement monitoring on "Deny" events
            # This will be done in another PR
            logger.warning("Incorrect authorization token received, dropping event.")
            deny_response = generate_policy('zoom_webhook', 'Deny', event['methodArn'])
            return deny_response

    # Default response
    return {
        'statusCode': 403,
        'body': json.dumps('Unauthorized.')
    }
