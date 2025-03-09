from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, name: str, description: str, **kwds):
        self.name = name
        self.description = description
        super().__init__(**kwds)

    @abstractmethod
    def execute(self, line: str):
        pass