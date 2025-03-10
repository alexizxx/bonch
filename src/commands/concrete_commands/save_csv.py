import csv
from src.bank_account import BankAccount
from src.commands.command import Command

class SaveCSV(Command):
    def __init__(self, receiver: BankAccount, **kwds):
        self.receiver = receiver
        super().__init__(**kwds) #Почитать про эту магию наследования-суперпозиции
        

    #save-csv OPTIONAL: path/
    def execute(self, line: str):
        args = line.split()
        if len(args) <= 2:
            path = "dummy_acc.csv"
            if len(args) == 2:
                path = args[1]

            #сохраняем в файл (ПЕРЕЗАПИСЫВАЕТ ФАЙЛ)
            with open(path, 'w',newline="", encoding='utf-8') as csv_file: 
                writer = csv.writer(csv_file, delimiter=" ")
                
                writer.writerow(["owner_name",self.receiver.get_owner_name()])
                writer.writerow(["id", self.receiver.get_id()])

                writer.writerow(["balance"])
                for curr, amount in self.receiver.get_balance().items():
                    writer.writerow([curr, amount])

        else:
            print("Incorrect argument count")
        pass

    def show_description(self):
        print(f"Save your account account-data to .csv file \n\tEXAMPLE: save-csv PATH \n\tSEMANTIC: PATH[OPTIONAL] (path to your file)")
        pass