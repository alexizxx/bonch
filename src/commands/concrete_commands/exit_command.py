from time import sleep
from src.bank_account import BankAccount
from src.commands.command import Command

class ExitCommand(Command):
    def __init__(self, receiver: BankAccount, **kwds):
        self.receiver = receiver
        super().__init__(**kwds) #Почитать про эту магию наследования-суперпозиции
        


    def execute(self, line: str):
        args = line.lower().split()
        if len(args) == 1:
            print("Thank you for using this app")
            print("Graceful shutdown...")
            sleep(0.5)
            exit(0)
        else:
            print("Incorrect argument count")