from abc import ABC, abstractmethod
import logging


class BaseEvent(ABC):
    def __init__(self, event=None, context=None, event_type="api-gw", logger=logging.getLogger(__name__)):
        self.event = event
        self.context = context
        self.type = event_type
        self.logger = logger
        super().__init__()

    @abstractmethod
    def parse(self):
        pass
