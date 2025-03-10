from src.commands.concrete_commands.load_csv import LoadCSV
from src.commands.concrete_commands.save_csv import SaveCSV
from src.bank_account import BankAccount, Currency
from src.commands.concrete_commands.exit_command import ExitCommand
from src.commands.concrete_commands.help_command import HelpCommand
from src.commands.concrete_commands.show_balance_command import ShowBalanceCommand
from src.commands.concrete_commands.show_command import ShowCommand
from src.commands.concrete_commands.withdraw_command import WithdrawCommand
from src.commands.invoker import Invoker
from src.commands.concrete_commands.deposit_command import DepositCommand

class Manager:
    def __init__(self, account: BankAccount, invoker: Invoker, ):
        self.receiver = account
        self.invoker = invoker
        self.initialize_invoker()

    #Внимательнее с receiver  
    def initialize_invoker(self):
        self.invoker.register("show", ShowCommand(receiver=self.invoker, name="show"))

        self.invoker.register("help", HelpCommand(receiver=self.invoker, name="help"))
        
        self.invoker.register("exit", ExitCommand(receiver=self.receiver, name="exit"))

        self.invoker.register("deposit", DepositCommand(receiver=self.receiver, name="deposit"))
        
        self.invoker.register("withdraw", WithdrawCommand(receiver=self.receiver, name="withdraw"))

        self.invoker.register("balance", ShowBalanceCommand(receiver=self.receiver, name="balance"))
        
        self.invoker.register("save-csv", SaveCSV(receiver=self.receiver, name="save-csv"))
        
        self.invoker.register("load-csv", LoadCSV(receiver=self.receiver, name="load-csv"))
        pass

    def execute_command(self, command_line: str):
        self.invoker.execute(command_line)
        pass