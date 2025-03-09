from enum import Enum

#Идея использовать строки в enum спорная, но хотелось попробовать
class Currency(Enum):
    DOL = "DOL"
    YEN = "YEN"
    RUB = "RUB"
    EUR = "EUR"
    
    

class BankAccount:
    _id_counter = 0  # >= 1, статический счетчик для присвоения id       

    def __init__(self, owner_name):
        BankAccount._id_counter += 1
        self._id = BankAccount._id_counter
        self._owner_name  = owner_name
        
        self._balance = dict() # словарь хранящихся валют
        for element in (Currency):
            self._balance.update({element : 0})

    #надо бы ПодумОть над названием метода
    #заменяет значения каждого поля объекта
    def change(self, owner_name, id, balance):
        self._id = id
        self._owner_name = owner_name
        self._balance = balance

    def deposit(self, amount, currency: Currency = Currency.RUB) -> bool:
        target = self._balance.get(currency) + amount
        self._balance.update({currency : target})

    def withdraw(self, amount, currency: Currency) -> bool:
        if self._balance.get(currency) >= amount:
            target = self._balance.get(currency) - amount
            self._balance.update({currency : target})
            return True
        else:
            return False

    def check_balance(self, currency: Currency = Currency.RUB) -> float:
        return self._balance.get(currency)        

    def get_balance(self) -> dict:
        return self._balance

    def get_id(self) -> int:
        return self._id
    
    def get_owner_name(self) -> str:
        return self._owner_name

    def __str__(self):
        return f'owner_name: {self._owner_name} id: {self._id}'
        pass