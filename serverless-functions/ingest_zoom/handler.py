import boto3
import logging
import os
import sys
import socket
import custom_logger
from . zoom_event_handler import ZoomEventHandler

REGION = os.getenv('REGION', 'us-west-2')
SERVICE = os.getenv('SERVICE')
sqs = boto3.client('sqs', region_name=REGION)


def setup_logging():
    logger = logging.getLogger()
    for h in logger.handlers:
        logger.removeHandler(h)
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(custom_logger.JsonFormatter(extra={"hostname": socket.gethostname()}))
    logger.addHandler(h)
    logger.setLevel(logging.INFO)
    return logger


def lambda_handler(event, context):
    logger = setup_logging()
    logger.info("{} is initialized.".format(SERVICE))

    zoom_event_handler = ZoomEventHandler(logger, region=REGION)
    handler_response = zoom_event_handler.process(event, context)
    return handler_response
