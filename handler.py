import boto3
import json
import logging
import os

REGION = os.getenv('REGION', 'us-west-2')
sqs = boto3.client('sqs', region_name=REGION)
ssm = boto3.client('ssm', region_name=REGION)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# The following code is incomplete, and only serves as a proof of concept.
def lambda_handler(event, context):
    if 'requestHeaders' in event:
        token = getZoomToken()
        if event['requestHeaders']['Authorization'] != token:
            return {
                'statusCode': 403,
                'body': json.dumps('Access is Denied')
            }
    if 'requestBody' in event:
        returnDict = dict()
        returnDict['details'] = {}
        returnDict['details']['participant'] = {}
        if 'payload' in event['requestBody']:
            if 'account_id' in event['requestBody']['payload']:
                returnDict['details']['account_id'] = event['requestBody']['payload']['account_id']
            if 'user_id' in event['requestBody']['payload']['object']['participant']:
                returnDict['details']['uid'] = event['requestBody']['payload']['object']['participant']['user_id']
            if 'user_name' in event['requestBody']['payload']['object']['participant']:
                returnDict['details']['participant']['username'] = event['requestBody']['payload']['object']['participant']['user_name']
            if 'join_time' in event['requestBody']['payload']['object']['participant']:
                returnDict['details']['participant']['join_time'] = event['requestBody']['payload']['object']['participant']['join_time']
            if 'id' in event['requestBody']['payload']['object']['participant'] and 'id' is not None:
                returnDict['details']['participant']['id'] = event['requestBody']['payload']['object']['participant']['id']
            if 'duration' in event['requestBody']['payload']['object']:
                returnDict['details']['duration'] = event['requestBody']['payload']['object']['duration']
            if 'start_time' in event['requestBody']['payload']['object']:
                returnDict['details']['start_time'] = event['requestBody']['payload']['object']['start_time']
            if 'timezone' in event['requestBody']['payload']['object']:
                returnDict['details']['timezone'] = event['requestBody']['payload']['object']['timezone']
            if 'id' in event['requestBody']['payload']['object']:
                returnDict['details']['meetingid'] = event['requestBody']['payload']['object']['id']
            if 'uuid' in event['requestBody']['payload']['object']:
                returnDict['details']['uuid'] = event['requestBody']['payload']['object']['uuid']
            if 'host_id' in event['requestBody']['payload']['object']:
                returnDict['details']['hostid'] = event['requestBody']['payload']['object']['host_id']
            if 'type' in event['requestBody']['payload']['object']:
                returnDict['details']['meeting_type'] = event['requestBody']['payload']['object']['type']
            if 'monitorTime' in event:
                returnDict['details']['timestamp'] = event['monitorTime']
        if 'event' in event['requestBody']:
            returnDict['summary'] = event['event']
        returnDict['source'] = 'zoom_api_aws_lambda'
        returnDict['category'] = 'zoom'
        returnDict['eventsource'] = 'zoom_api'
        returnDict['hostname'] = 'marketplace.zoom.us'
        returnDict['tags'] = 'zoom'
        returnDict['processname'] = 'zoomconnect'
        returnDict['processid'] = 'none'
        returnDict['severity'] = 'INFO'

    queue = sqs.get_queue_by_name(QueueName='placeholder') # Need to add queue name to env vars or ssm parameter store
    response = queue.send_message(MessageBody=json.dumps(returnDict))
    return {
        'statusCode': 200,
        'body': json.dumps('Event received')
    }


def getZoomToken(self):
    try:
        logger.info("Obtaining Zoom auth token from SSM.")
        response = ssm.get_parameter(Name="/mozdef-event-framework/ZOOM_AUTH_TOKEN", WithDecryption=True)
        zoom_token = response['Parameter']['Value']
        return zoom_token
    except Exception as e:
        logger.error("A problem occurred while accessing SSM, exception:{}".format(e.value))
