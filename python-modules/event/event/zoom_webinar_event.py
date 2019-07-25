import logging
import json
from event import BaseEvent


class ZoomWebinarEvent(BaseEvent):
    def __init__(self, event=None, context=None, logger=logging.getLogger(__name__)):
        super().__init__()

    def parse(self):

        return True