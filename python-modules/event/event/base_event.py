from abc import ABC, abstractmethod
import logging


class BaseEvent(ABC):
    def __init__(self, event=None, context=None, logger=logging.getLogger(__name__)):
        self.event = event
        self.context = context
        self.type = "api-gw"
        self.logger = logger
        super().__init__()

    @abstractmethod
    def parse(self):
        pass
