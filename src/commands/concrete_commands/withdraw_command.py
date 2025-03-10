from src.bank_account import BankAccount, Currency
from src.commands.command import Command

class WithdrawCommand(Command):
    def __init__(self, receiver: BankAccount, **kwds):
        self.receiver = receiver
        super().__init__(**kwds) #Почитать про эту магию наследования-суперпозиции
        

    #line - строка.strip() введенная пользователем line[0] - имя команды
    def execute(self, line: str):
        args = line.upper().split() #upper() - Стилизация, чтобы работало: yena YENA Yena YeNa
        if len(args) == 3:
            try:
                amount = int(args[1])
                if amount < 0:
                    raise ValueError("Amount must be a greater then 0")
                
                currency = args[2]

                for element in (Currency):
                    if element.value == currency:
                        break
                else:
                    raise ValueError("Incorrect currency")
                
            except ValueError as msg:
                print(msg)
            else:
                currency = Currency(currency)
                if self.receiver.withdraw(amount, currency):
                    print("Operation successful")
                else:
                    print("You have not money for withdraw, try deposit something before")
        else:
            print("Incorrect argument count")


    def show_description(self):
        print(f"Withdraw money from your account \n\tEXAMPLE: withdraw AMOUNT CURRENCY \n\tSEMANTIC: AMOUNT (int > 0), CURRENCY: {[e.value for e in Currency]}")
        pass