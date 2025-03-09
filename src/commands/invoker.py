from src.commands.command import Command

class Invoker:
    def __init__(self):
        self.command_map = dict()
        
    def register(self, command_name: str, command: Command):
        self.command_map.update({command_name : command})


    def execute(self, command_line: str):
            try:
                command = self.command_map.get(command_line.split()[0])
            except IndexError: #Если ввели пустую строку
                print("Command not found")
            else:
                if command is None:
                    print("Incorrect command, try again (or use \"show\" to get more information)")
                    return
                command.execute(command_line)
    