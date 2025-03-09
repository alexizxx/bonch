from src.bank_account import BankAccount
from src.commands.manager import Manager
from src.commands.invoker import Invoker

def main():
    account = BankAccount("Maria")
    manager = Manager(account, Invoker())
    #
    print(account)
    manager.start()
    pass

if __name__ == "__main__":
    main()