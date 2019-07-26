import logging
import json
from event import BaseEvent


class ZoomUserEvent(BaseEvent):
    def __init__(self, event=None, context=None, event_type="zoom", logger=logging.getLogger(__name__)):
        self.event = event
        self.mozdef_message = None
        self.zoom_event = None
        self.payload = None
        self.payload_object = None
        assert self.parse()
        super().__init__()

    def parse(self):
        if (self._valid_type() & self._event_payload_exists() & self._valid_payload()):
            self.mozdef_message = dict()
            self.mozdef_message['details'] = {}
            self.mozdef_message['summary'] = self.event.get('event')
            self.mozdef_message['source'] = 'zoom_api_aws_lambda'
            self.mozdef_message['category'] = 'zoom'
            self.mozdef_message['eventsource'] = 'zoom_api'
            self.mozdef_message['hostname'] = 'marketplace.zoom.us'
            self.mozdef_message['tags'] = 'zoom'
            self.mozdef_message['processname'] = 'zoomconnect'
            self.mozdef_message['processid'] = 'none'
            self.mozdef_message['severity'] = 'INFO'

            self.mozdef_message['details']['account_id'] = self.payload.get('account_id')
            self.mozdef_message['details']['duration'] = self.payload_object.get('duration')
            self.mozdef_message['details']['start_time'] = self.payload_object.get('start_time')
            self.mozdef_message['details']['timezone'] = self.payload_object.get('timezone')
            self.mozdef_message['details']['topic'] = self.payload_object.get('topic')
            self.mozdef_message['details']['id'] = self.payload_object.get('id')
            self.mozdef_message['details']['type'] = self.payload_object.get('type')
            self.mozdef_message['details']['uuid'] = self.payload_object.get('uuid')
            self.mozdef_message['detials']['host_id'] = self.payload_object.get('host_id')
            return True
        else:
            return False

    def _valid_type(self):
        # It must be a dict
        if not isinstance(self.event, dict):
            return False
        return True

    def _event_payload_exists(self):
        # Zoom event must have a payload
        if 'payload' not in self.event:
            return False
        # Payload must be a dict
        if not isinstance(self.event['payload'], dict):
            return False
        return True

    def _valid_payload(self):
        invalid = False
        self.payload = self.event['payload']
        # Zoom event payload must have account_id and object
        if 'account_id' not in self.payload or 'object' not in self.payload:
            return False
        if not isinstance(self.payload['account_id'], str):
            return False
        if not isinstance(self.payload['object'], dict):
            return False
        self.payload_object = self.payload['object']
        if len(self.payload_object) != 8:
            return False
        object_fields = [
            'duration', 'start_time', 'timezone',
            'topic', 'id', 'type',
            'uuid', 'host_id'
        ]
        for field in object_fields:
            if field not in self.payload_object.keys():
                invalid = True
                break
        if invalid:
            return False

        # Do we need to perform type checking here also for values of keys?

        # If all OK until now, we have a valid Zoom user event
        return True
