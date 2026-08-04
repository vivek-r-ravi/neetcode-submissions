"""
Python provides a more idiomatic way to use getters and setters using the @property and @setter decorators.

Instead of having two methods get_balance and set_balance, just use one function
balance, used with a property or attribute.setter decorator, making the code cleaner, feeling more natural like using attributes

Remember to keep the name of the attribute the same for both the getter and setter methods
"""


class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance  # Don't modify this line

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
