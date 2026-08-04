class BankAccount:
    def __init__(self, balance: int): 
        self.__balance = balance # Don't modify this line
        
    @property
    def balance(self) -> int:
        return self.__balance
    
    @balance.setter
    def balance(self, value: int) -> None:
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative!")


# Don't modify the code below this line
account = BankAccount(1000)
print(account.balance)
account.balance = -100
