from src.commands.manager import Manager


class Console:
    
    def __init__(self):
        pass

    def display_welcome_message(self, owner_name: str):
        print(f"Hello {owner_name} here is the cli for managing your Bank account!")
        print("You might use command 'show' to get more information")
        print("Enjoyable use!")
        pass

    def interactive_step(self, instance : Manager):
        try:
            line_args = input("\n>> ").strip()
        except KeyboardInterrupt:
            instance.execute_command("exit")
        else:
            instance.execute_command(line_args)
        pass

    def start(self, instance : Manager):
        self.display_welcome_message(instance.receiver.get_owner_name())
        while True:
            self.interactive_step(instance)
        pass