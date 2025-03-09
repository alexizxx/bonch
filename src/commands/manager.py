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
        self.invoker.register("show", ShowCommand(receiver=self.invoker,
                                                name="show",
                                                description="Describe short information about all commands"))
        
        self.invoker.register("exit", ExitCommand(receiver=self.receiver,
                                                name="exit",
                                                description="Exit the session"))
        
        self.invoker.register("help", HelpCommand(receiver=self.invoker,
                                                  name="help",
                                                  description="Describe information about concrete command\n\t EXAMPLE: help COMMAND \n\tSEMANTIC: COMMAND ('show'/'exit'/'deposit')"))

        self.invoker.register("deposit", DepositCommand(receiver=self.receiver,
                                                name="deposit",
                                                description=f"Deposit money to your account \n\tEXAMPLE: deposit AMOUNT CURRENCY \n\tSEMANTIC: AMOUNT (int > 0), CURRENCY: {[e.value for e in Currency]}"))
        self.invoker.register("withdraw", WithdrawCommand(receiver=self.receiver,
                                                name="withdraw",
                                                description=f"Withdraw money from your account \n\tEXAMPLE: withdraw AMOUNT CURRENCY \n\tSEMANTIC: AMOUNT (int > 0), CURRENCY: {[e.value for e in Currency]}"))


        self.invoker.register("balance", ShowBalanceCommand(receiver=self.receiver,
                                                            name="balance",
                                                            description="Show your balance"))
        pass
    
    def execute_command(self, command_line: str):
        self.invoker.execute(command_line)

    def display_welcome_message(self):
        print(f"Hello {self.receiver.get_owner()} here is the cli for managing your Bank account!")
        print("You might use command 'show' to get more information")
        print("Enjoyable use!")
        pass

    def interactive_step(self):
        try:
            line_args = input("\n>> ").strip()
        except KeyboardInterrupt:
            self.execute_command("exit")
        else:
            self.execute_command(line_args)
        pass

    def start(self):
        self.display_welcome_message()
        while True:
            self.interactive_step()
        pass