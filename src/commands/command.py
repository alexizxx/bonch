from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, name: str, **kwds):
        self.name = name
        super().__init__(**kwds)

    @abstractmethod
    def execute(self, line: str):
        pass

    @abstractmethod
    def show_description(self):
        pass