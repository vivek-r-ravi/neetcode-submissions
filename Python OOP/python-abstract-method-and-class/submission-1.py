"""
An abstract method is a method that is declared in a base class, but contains no implementation. The child class must implement the abstract method. Abstract methods are used to enforce a contract on subclasses. Subclasses must implement the abstract method, otherwise they will raise an error.

An abstract class is a class that contains one or more abstract methods. It serves as a blueprint for other classes and cannot be instantiated on its own.

Python's abc module provides support for abstract method and abstract class.

In the below example, 
* PaymentCard is the base abstract class that inherits from ABC. In python, abstract classes are created by inheriting from ABC.
* The @abstractmethod decorator marks process_payment() as an abstract method. In Python, abstract methods are created by decorating a method with @abstractmethod decorator.
* CreditCard, DebitCard and any other child class that inherits from PaymentCard, must implement the process_payment() method.
* Non-abstract methods like get_balance() are optional to override.

Note you can't create an instance of PaymentCard class because it is an abstract class and has an abstract method.

hero = PaymentCard("1234", 100.0)
This will raise a TypeError because the process_payment() method is not implemented.

Abstract methods are a powerful tool for achieving abstraction because they:

* Hide implementation details (abstraction): The base class only declares what methods must exist, without specifying how they work.
* Enforce consistency: Child classes must implement these methods, ensuring a standard interface across all subclasses, which allows for polymorphism.
* Prevent incomplete objects: You can't create instances of classes with abstract methods, ensuring only fully-implemented classes can be used.
"""


from abc import ABC, abstractmethod


class PaymentCard(ABC):
    def __init__(self, card_number: str, balance: float):
        self.card_number = card_number
        self.balance = balance

    def get_balance(self) -> float:
        return self.balance

    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass


class DebitCard(PaymentCard):
    def process_payment(self, amount: float) -> str:
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return "Payment successful"


class CreditCard(PaymentCard):
    def process_payment(self, amount: float) -> str:
        self.balance -= amount
        return "Payment successful"


# Don't modify the code below
debit_card = DebitCard("1234", 100.0)  # Card with $100 balance
credit_card = CreditCard("5678", 100.0)  # Card with $100 balance

# Test debit card
print(debit_card.process_payment(50.0))
print(debit_card.balance)
print(debit_card.process_payment(100.0))
print(debit_card.balance)

# Test credit card
print(credit_card.process_payment(50.0))
print(credit_card.balance)
print(credit_card.process_payment(100.0))
print(credit_card.balance)
