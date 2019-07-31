import logging
import json
from event.zoom import ZoomEvent


class ZoomAccountEvent(ZoomEvent):
    def __init__(self, event=None, context=None, zoom_event_type=None, logger=logging.getLogger(__name__)):
        self.mozdef_message = {}
        super().__init__()

    def validate(self):
        super.validate()

    def parse(self):
        return True
