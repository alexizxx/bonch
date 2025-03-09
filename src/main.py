from src.console import Console
from src.bank_account import BankAccount
from src.commands.manager import Manager
from src.commands.invoker import Invoker

def main():
    console = Console()

    account = BankAccount("Maria")
    manager = Manager(account, Invoker())
    #
    print(account)
    console.start(manager)
    pass

if __name__ == "__main__":
    main()