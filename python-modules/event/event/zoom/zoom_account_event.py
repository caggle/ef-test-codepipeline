import logging
import json
from event import ZoomEvent


class ZoomAccountEvent(ZoomEvent):
    def __init__(self, event=None, context=None, zoom_event_type=None, logger=logging.getLogger(__name__)):
        super().__init__()

    def validate(self):
        super.validate()

    def parse(self):
        # This is where we actually parse and get
        # values from the Zoom event
        return True
