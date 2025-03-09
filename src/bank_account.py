from enum import Enum

#Идея использовать строки в enum спорная, но хотелось попробовать
class Currency(Enum):
    DOL = "DOL"
    YEN = "YEN"
    RUB = "RUB"
    EUR = "EUR"
    
    

class BankAccount:
    _id_counter = 0 # >= 1, статический счетчик для присвоения id       

    def __init__(self, owner):
        BankAccount._id_counter += 1
        self._id = BankAccount._id_counter
        self._owner = owner
        
        self.balance = dict() # словарь хранящихся валют
        for element in (Currency):
            self.balance.update({element : 0})

    def deposit(self, amount, currency: Currency = Currency.RUB):
        target = self.balance.get(currency) + amount
        self.balance.update({currency : target})

    def withdraw(self, amount, currency: Currency):
        if self.balance.get(currency) >= amount:
            target = self.balance.get(currency) - amount
            self.balance.update({currency : target})
            return True
        else:
            return False

    def check_balance(self, currency: Currency = Currency.RUB):
        return self.balance.get(currency)        

    def get_balance(self):
        return self.balance

    def get_id(self):
        return self.id
    
    def get_owner(self):
        return self._owner

    def __str__(self):
        return f'Owner: {self._owner}, ID: {self._id}'
        pass