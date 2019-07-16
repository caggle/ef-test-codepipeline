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
    if 'headers' in event:
        token = getZoomToken()
        if event['headers']['Authorization'] != token:
            return {
                'statusCode': 403,
                'body': json.dumps('Access is Denied')
            }
    else:
        return {
            'statusCode': 403,
            'body': json.dumps('Access is Denied')
        }

    if 'body' in event:
        returnDict = dict()
        returnDict['details'] = {}
        returnDict['details']['participant'] = {}
        if 'payload' in event['body']:
            if 'account_id' in event['body']['payload']:
                returnDict['details']['account_id'] = event['body']['payload']['account_id']
            if 'user_id' in event['body']['payload']['object']['participant']:
                returnDict['details']['uid'] = event['body']['payload']['object']['participant']['user_id']
            if 'user_name' in event['body']['payload']['object']['participant']:
                returnDict['details']['participant']['username'] = event['body']['payload']['object']['participant']['user_name']
            if 'join_time' in event['body']['payload']['object']['participant']:
                returnDict['details']['participant']['join_time'] = event['body']['payload']['object']['participant']['join_time']
            if 'id' in event['body']['payload']['object']['participant'] and 'id' is not None:
                returnDict['details']['participant']['id'] = event['body']['payload']['object']['participant']['id']
            if 'duration' in event['body']['payload']['object']:
                returnDict['details']['duration'] = event['body']['payload']['object']['duration']
            if 'start_time' in event['body']['payload']['object']:
                returnDict['details']['start_time'] = event['body']['payload']['object']['start_time']
            if 'timezone' in event['body']['payload']['object']:
                returnDict['details']['timezone'] = event['body']['payload']['object']['timezone']
            if 'id' in event['body']['payload']['object']:
                returnDict['details']['meetingid'] = event['body']['payload']['object']['id']
            if 'uuid' in event['body']['payload']['object']:
                returnDict['details']['uuid'] = event['body']['payload']['object']['uuid']
            if 'host_id' in event['body']['payload']['object']:
                returnDict['details']['hostid'] = event['body']['payload']['object']['host_id']
            if 'type' in event['body']['payload']['object']:
                returnDict['details']['meeting_type'] = event['body']['payload']['object']['type']
            if 'monitorTime' in event:
                returnDict['details']['timestamp'] = event['monitorTime']
        if 'event' in event['body']:
            returnDict['summary'] = event['body']['event']
            returnDict['source'] = 'zoom_api_aws_lambda'
            returnDict['category'] = 'zoom'
            returnDict['eventsource'] = 'zoom_api'
            returnDict['hostname'] = 'marketplace.zoom.us'
            returnDict['tags'] = 'zoom'
            returnDict['processname'] = 'zoomconnect'
            returnDict['processid'] = 'none'
            returnDict['severity'] = 'INFO'

        queueURL = os.getenv('SQS_URL')   # Obtaining the queue as environment variable
        response = sqs.send_message(QueueUrl=queueURL, queueMessageBody=json.dumps(returnDict))
        return {
            'statusCode': 200,
            'body': json.dumps('Event received')
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Bad Request')
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
