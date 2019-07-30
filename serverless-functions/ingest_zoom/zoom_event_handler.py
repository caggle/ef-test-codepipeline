import boto3
import json
import logging
import os
from response import Response
from event.aws.aws_event import AWSEvent
from event.zoom.zoom_account_event import ZoomAccountEvent
from event.zoom.zoom_meeting_event import ZoomMeetingEvent
from event.zoom.zoom_recording_event import ZoomRecordingEvent
from event.zoom.zoom_rooms_event import ZoomRoomsEvent
from event.zoom.zoom_user_event import ZoomUserEvent
from event.zoom.zoom_webinar_event import ZoomWebinarEvent
from event.zoom.zoom_event import ZoomEvent

REGION = os.getenv('REGION', 'us-west-2')
sqs = boto3.client('sqs', region_name=REGION)


class ZoomEventHandler(object):
    def __init__(
        self,
        sqs_client=boto3.client('sqs', region_name='us-west-2'),
        queueURL=os.getenv('SQS_URL'),
        logger=logging.getLogger(__name__),
        region='us-west-2'
    ):
        self.region = region
        self.queueURL = queueURL
        self.sqs_client = sqs_client
        self.logger = logger

    def send_to_mozdef(self, zoom_event):
        queueURL = os.getenv('SQS_URL')   # Obtaining the queue as environment variable
        sqs.send_message(QueueUrl=queueURL, MessageBody=json.dumps(zoom_event))

    def process(self, event, context):
        failed = False
        root_event = AWSEvent(event, context, self.logger)
        zoom_data = root_event.parse()
        if not zoom_data:
            self.logger.error("Unrecognized payload: {}".format(zoom_data))
            # Add to DLQ here?
            return Response({
                    'statusCode': 400,
                    'body': json.dumps({'Bad Request'})
                }).with_security_headers()
        else:
            if 'event' not in zoom_data or 'payload' not in zoom_data:
                self.logger.error("AWS event does not contain Zoom event data.")
                # Add to DLQ here?
                return Response({
                    'statusCode': 400,
                    'body': json.dumps({'Bad Request'})
                }).with_security_headers()

            zoom_event_type, detail = zoom_data['event'].split('.')
            if "meeting" in zoom_event_type:
                # Create Zoom Meeting Event object
                return False
            elif "recording" in zoom_event_type:
                # Create Zoom Recording Event object
                return False
            elif "user" in zoom_event_type:
                # Create Zoom User Event object
                try:
                    valid_event = ZoomUserEvent(zoom_data, event_sub_type=zoom_data['event'], logger=self.logger)
                except Exception:
                    # Add to DLQ here
                    failed = True
            elif "account" in zoom_event_type:
                # Create Zoom Account Event object
                return False
            elif "webinar" in zoom_event_type:
                # Create Zoom Webinar Event object
                return False
            elif "room" in zoom_event_type:
                # Create Zoom Room Event object
                return False

            if failed:
                return Response({
                    'statusCode': 400,
                    'body': json.dumps({'Bad Request'})
                }).with_security_headers()
            else:
                self.send_to_mozdef(valid_event)
                return Response({
                    'statusCode': 200,
                    'body': json.dumps({'Event received'})
                }).with_security_headers()
