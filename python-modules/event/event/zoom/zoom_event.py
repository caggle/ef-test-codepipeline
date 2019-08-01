import logging
import json
import fastjsonschema
from pathlib import Path
from event import BaseEvent
from event.zoom.schemas.zoom_user_schemas import *


class ZoomEvent(BaseEvent):
    def __init__(self, event=None, context=None, zoom_event_type=None, logger=logging.getLogger(__name__)):
        self.event = event
        self.valid_event = None
        self.zoom_event_type = "zoom_" + zoom_event_type
        assert self.validate()
        super().__init__()

    def validate(self):
        # Try to load schema. We can consider loading this
        # from somewhere else, maybe from an S3 bucket that
        # polls the Zoom schema regularly for updates?

        zoom_schema_validator = fastjsonschema.compile(self._load_full_schema())
        try:
            self.valid_event = zoom_schema_validator(self.event)
        except fastjsonschema.JsonSchemaException:
            self.logger.error("Error while validating event against Zoom schema.")
            return False
        else:
            return True

    def _load_full_schema(self):
        repo_dir = Path(__file__).resolve().parents[3]
        full_zoom_schema = repo_dir.joinpath('schemas/ZoomEventInputModel.json')

        with open(full_zoom_schema, 'r') as fh:
            zoom_schema = json.loads(fh.read())

        return zoom_schema
