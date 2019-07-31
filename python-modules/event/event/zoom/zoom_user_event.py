import logging
import json
from event.zoom import ZoomEvent


class ZoomUserEvent(ZoomEvent):
    def __init__(self, event=None, context=None, zoom_event_type=None, logger=logging.getLogger(__name__)):
        self.mozdef_message = {}
        super().__init__()

    def validate(self):
        super.validate()

    def parse(self):
        # Main meat, which will be a part of all MozDef messages
        self.mozdef_message['details'] = {}
        self.mozdef_message['summary'] = self.event.get('event', '')
        self.mozdef_message['source'] = 'zoom_api_aws_lambda'
        self.mozdef_message['category'] = 'zoom'
        self.mozdef_message['eventsource'] = 'zoom_api'
        self.mozdef_message['hostname'] = 'marketplace.zoom.us'
        self.mozdef_message['tags'] = 'zoom'
        self.mozdef_message['processname'] = 'zoomconnect'
        self.mozdef_message['processid'] = 'none'
        self.mozdef_message['severity'] = 'INFO'

        if "created" in self.zoom_event_type:
            self.parse_user_created()
        elif "updated" in self.zoom_event_type:
            self.parse_user_updated()
        elif "settings" in self.zoom_event_type:
            self.parse_user_settings_updated()
        elif "activated" in self.zoom_event_type:
            # Note this will handle 2 events (activate and deactivate)
            self.parse_user_activity()
        elif "disassociate" in self.zoom_event_type:
            self.parse_user_disassociated()
        elif "deleted" in self.zoom_event_type:
            self.parse_user_deleted()
        else:
            self.logger.error("Unknown Zoom event.")
            return False
        return self.mozdef_message

    def parse_user_created(self):
        # Event details specific for event type
        self.mozdef_message['details']['account_id'] = self.event['payload'].get('account_id', '')
        self.mozdef_message['details']['operator'] = self.event['payload'].get('operator', '')
        self.mozdef_message['details']['creation_type'] = self.event['payload'].get('creation_type', '')
        self.mozdef_message['details']['id'] = self.event['payload'].get('object').get('id', '')
        self.mozdef_message['details']['first_name'] = self.event['payload'].get('object').get('first_name', '')
        self.mozdef_message['details']['last_name'] = self.event['payload'].get('object').get('last_name', '')
        self.mozdef_message['details']['email'] = self.event['payload'].get('object').get('email', '')
        self.mozdef_message['details']['type'] = self.event['payload'].get('object').get('type', '')

    def parse_user_updated(self):
        # Event details specific for event type
        return True

    #     if (self._valid_type() & self._event_payload_exists() & self._valid_payload()):
    #         self.mozdef_message = dict()
    #         self.mozdef_message['details'] = {}
    #         self.mozdef_message['summary'] = self.event.get('event')
    #         self.mozdef_message['source'] = 'zoom_api_aws_lambda'
    #         self.mozdef_message['category'] = 'zoom'
    #         self.mozdef_message['eventsource'] = 'zoom_api'
    #         self.mozdef_message['hostname'] = 'marketplace.zoom.us'
    #         self.mozdef_message['tags'] = 'zoom'
    #         self.mozdef_message['processname'] = 'zoomconnect'
    #         self.mozdef_message['processid'] = 'none'
    #         self.mozdef_message['severity'] = 'INFO'

    #         self.mozdef_message['details']['account_id'] = self.payload.get('account_id')
    #         self.mozdef_message['details']['duration'] = self.payload_object.get('duration')
    #         self.mozdef_message['details']['start_time'] = self.payload_object.get('start_time')
    #         self.mozdef_message['details']['timezone'] = self.payload_object.get('timezone')
    #         self.mozdef_message['details']['topic'] = self.payload_object.get('topic')
    #         self.mozdef_message['details']['id'] = self.payload_object.get('id')
    #         self.mozdef_message['details']['type'] = self.payload_object.get('type')
    #         self.mozdef_message['details']['uuid'] = self.payload_object.get('uuid')
    #         self.mozdef_message['detials']['host_id'] = self.payload_object.get('host_id')
    #         return True
    #     else:
    #         return False

    # def _event_payload_exists(self):
    #     # The event must have a payload
    #     if 'payload' not in self.event:
    #         return False
    #     # Payload must be a dict
    #     if not isinstance(self.event['payload'], dict):
    #         return False
    #     return True

    # def _valid_payload(self):
    #     # All Zoom User events at least have "account_id", "operator" and "object" fields
    #     self.payload = self.event['payload']
    #     if 'account_id' not in self.payload or 'object' not in self.payload or 'operator' not in self.payload:
    #         return False
    #     if not isinstance(self.payload['account_id'], str):
    #         return False
    #     if not isinstance(self.payload['operator'], str):
    #         return False
    #     if not isinstance(self.payload['object'], dict):
    #         return False
    #     return True

    # def _valid_payload_object(self):
    #     invalid = False
    #     self.payload_object = self.event['payload']['object']

    #     if self.zoom_event_type == "created":
    #         if len(self.payload_object) != 5:
    #             return False
    #         object_fields = [
    #             'id', 'first_name',
    #             'last_name', 'email',
    #             'type'
    #         ]
    #         for field in object_fields:
    #             if field not in self.payload_object.keys():
    #                 invalid = True
    #                 break
    #         if invalid:
    #             return False

    #     self.payload = self.event['payload']
    #     # Zoom event payload must have account_id and object
    #     if 'account_id' not in self.payload or 'object' not in self.payload:
    #         return False
    #     if not isinstance(self.payload['account_id'], str):
    #         return False
    #     if not isinstance(self.payload['object'], dict):
    #         return False
    #     self.payload_object = self.payload['object']
    #     if len(self.payload_object) != 8:
    #         return False
    #     object_fields = [
    #         'duration', 'start_time', 'timezone',
    #         'topic', 'id', 'type',
    #         'uuid', 'host_id'
    #     ]
    #     for field in object_fields:
    #         if field not in self.payload_object.keys():
    #             invalid = True
    #             break
    #     if invalid:
    #         return False

    #     # Do we need to perform type checking here also for values of keys?

    #     # If all OK until now, we have a valid Zoom user event
    #     return True
