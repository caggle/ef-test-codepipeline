import logging
import json
from event import BaseEvent


class AWSEvent(BaseEvent):
    def __init__(self, event=None, context=None, event_type="api-gw", logger=logging.getLogger(__name__)):
        super().__init__()

    def parse(self):
        try:
            json.loads(self.event['body'])
        except Exception as e:
            self.logger.error("Cannot parse event: {}, context: {}, exception: ".format(str(self.event), self.context.function_name, e))
            self.type = "invalid"
            # Add event here to the DLQ?
            return False
        else:
            # Return what is relevant for further processing,
            #  i.e. POST request body from Zoom web hook
            return json.loads(self.event['body'])
