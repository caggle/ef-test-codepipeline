import boto3
import json
import logging
import os

REGION = os.getenv('REGION', 'us-west-2')
sqs = boto3.client('sqs', region_name=REGION)
ssm = boto3.client('ssm', region_name=REGION)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# The following code is incomplete, and only serves as a proof of concept.
def lambda_handler(event, context):
    token = getZoomToken()
    if event['headers']['Authorization'] != token:
        return {
            'statusCode': 403,
            'body': json.dumps('Access is Denied')
        }
    if 'body' in event:
        returnDict = dict()
        returnDict['details'] = {}
        zoom_event = json.loads(event['body'])
        if 'event' not in zoom_event or 'payload' not in zoom_event:
            return {
                'statusCode': 400,
                'body': json.dumps('Bad Request')
            }

        returnDict['summary'] = zoom_event['event']
        returnDict['source'] = 'zoom_api_aws_lambda'
        returnDict['category'] = 'zoom'
        returnDict['eventsource'] = 'zoom_api'
        returnDict['hostname'] = 'marketplace.zoom.us'
        returnDict['tags'] = 'zoom'
        returnDict['processname'] = 'zoomconnect'
        returnDict['processid'] = 'none'
        returnDict['severity'] = 'INFO'

        if 'payload' in zoom_event:
            if 'account_id' in zoom_event['payload']:
                returnDict['details']['account_id'] = zoom_event['payload']['account_id']
            if 'operator' in zoom_event['payload']:
                returnDict['details']['operator'] = zoom_event['payload']['operator']
            if 'operator_id' in zoom_event['payload']:
                returnDict['details']['operator_id'] = zoom_event['payload']['operator_id']
            if 'object' in zoom_event['payload']:
                if 'id' in zoom_event['payload']['object']:
                    returnDict['details']['id'] = zoom_event['payload']['object']['id']
                if 'owner_id' in zoom_event['payload']['object']:
                    returnDict['details']['owner_id'] = zoom_event['payload']['object']['owner_id']
                if 'owner_email' in zoom_event['payload']['object']:
                    returnDict['details']['owner_email'] = zoom_event['payload']['object']['owner_email']

        queueURL = os.getenv('SQS_URL')   # Obtaining the queue as environment variable
        sqs.send_message(QueueUrl=queueURL, MessageBody=json.dumps(returnDict))
        return {
            'statusCode': 200,
            'body': json.dumps('Event received')
        }


def getZoomToken():
    try:
        logger.info("Obtaining Zoom auth token from SSM.")
        response = ssm.get_parameter(Name="/mozdef-event-framework/ZOOM_AUTH_TOKEN", WithDecryption=True)
        zoom_token = response['Parameter']['Value']
        return zoom_token
    except Exception as e:
        logger.error("A problem occurred while accessing SSM, exception: {}".format(e))
        return False
