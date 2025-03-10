import csv
from src.bank_account import BankAccount, Currency
from src.commands.command import Command

class LoadCSV(Command):
    def __init__(self, receiver: BankAccount, **kwds):
        self.receiver = receiver
        super().__init__(**kwds) #Почитать про эту магию наследования-суперпозиции
        

    #load-csv OPTIONAL: path/
    #   FILE-STRUCT
    #---------------------------
    #   owner_name: (str)
    #   id: (int)
    #   balance:
    #   CUR[0] (str) AMOUNT (float)
    #   CUR[1] (str) AMOUNT (float)
    #...
    #----------------------------
    #Стоит доработать
    def execute(self, line: str):
        args = line.split()
        if len(args) <= 2:
            path = "dummy_acc.csv"
            if len(args) == 2:
                path = args[1]
            
            try:
                with open(path, "r") as csv_file:
                    reader = csv.reader(csv_file, delimiter=" ")

                    fields = {
                        "owner_name" : "",
                        "id" : int,
                        "balance" : dict()
                    }

                    

                    #Тут очевидно не лучшее решение, еще подумать
                    #
                    try:
                        for row in reader:
                            if row[0].startswith("balance"):
                                continue
                            
                            if row[0].startswith("Currency."):
                                row[0] = row[0].rpartition(".")[2]#Разбиваем строку вида Currency.DOL на ['Currency', '.', 'DOL'] и берем DOL 
                                for name, member in Currency.__members__.items():
                                    if member.name.startswith(row[0]):
                                        currency = member
                                amount = int(row[1])
                                fields["balance"].update({currency : amount})
                            else:
                                fields[row[0]] = row[1]

                            pass

                        self.receiver.change(fields["owner_name"], fields["id"], fields["balance"])
                        print(f"Succesfull load \nhello {self.receiver.get_owner_name()}")
                    except KeyError as error:
                        print("Invalid file format can't find the balance")
                    except UnboundLocalError as error:
                        print("Invalid file format can't cast value to currency")
                    except ValueError as error:
                        print("Invalid file format can't cast value to integer!")
                    except Exception as error:
                        print ("Invalid file format")
                        return
            
                    pass          
            except IOError as error:
                print(error)

        else:
            print("Incorrect argument count")
            pass

    def show_description(self):
        print(f"Load from account-data .csv to account and change it instantly \n\tEXAMPLE: load-csv PATH \n\tSEMANTIC: PATH[OPTIONAL] (path to your file)")
        pass