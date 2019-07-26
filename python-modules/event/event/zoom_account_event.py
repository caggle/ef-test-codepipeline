import logging
import json
from event import BaseEvent


class ZoomAccountEvent(BaseEvent):
    def __init__(self, zoom_event=None, context=None, event_type="zoom", logger=logging.getLogger(__name__)):
        assert self.parse(zoom_event)
        super().__init__()

    def parse(self):
        # Many assertions here?

        return True
