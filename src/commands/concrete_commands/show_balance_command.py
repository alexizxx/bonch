from src.bank_account import BankAccount
from src.commands.command import Command

class ShowBalanceCommand(Command):
    def __init__(self, receiver: BankAccount, **kwds):
        self.receiver = receiver
        super().__init__(**kwds) #Почитать про эту магию наследования-суперпозиции
        


    def execute(self, line: str):
        args = line.lower().split()
        if len(args) == 1:
            print("Your balance now:")
            for a, b in self.receiver.get_balance().items():
                print(f'\t{a.value.upper()} : {b}')
        else:
            print("Incorrect argument count")