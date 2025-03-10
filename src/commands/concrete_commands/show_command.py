from src.commands.command import Command
from src.commands.invoker import Invoker

class ShowCommand(Command):
    def __init__(self, receiver: Invoker, **kwds):
        self.receiver = receiver
        super().__init__(**kwds) #Почитать про эту магию наследования-суперпозиции
        


    def execute(self, line: str):
        args = line.lower().split()
        if len(args) == 1:
            print('Description of all commands:')
            for a, b in self.receiver.command_map.items():
                print(f'{a} - ', end="")
                b.show_description()
        else:
            print("Incorrect argument count")

    def show_description(self):
        print(f"Describe short information about all commands")
        pass