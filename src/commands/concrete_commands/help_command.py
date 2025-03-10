from src.commands.command import Command
from src.commands.invoker import Invoker

class HelpCommand(Command):
    def __init__(self, receiver: Invoker, **kwds):
        self.receiver = receiver
        super().__init__(**kwds) #Почитать про эту магию наследования-суперпозиции
        


    def execute(self, line: str):
        args = line.lower().split()
        if len(args) == 2:
            if isinstance(self.receiver.command_map.get(args[1]), Command):
                print(f'{args[1]}  -  {self.receiver.command_map.get(args[1]).description}')
            else:
                print("Incorrect command name")
        else:
            print("Incorrect argument count")

    def show_description(self):
        print(f"Describe information about concrete command\n\tEXAMPLE: help COMMAND \n\tSEMANTIC: COMMAND ('show'/'exit'/'deposit')")
        pass
            