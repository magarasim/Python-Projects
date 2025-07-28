# simulate a bank operation of depositing, withdrawing and balancing inquiry.
# Create a class BankAccount with methods: deposit(), withdraw(), check_balance().
# use encapsulation to protect the balance attribute. 
# Create a child class like savings account and CurrentAccount account using inheritance.
# Use super() to call the parent constructor from the child class. 
# Implement abstraction to define a generic account that cannot be instantiated directly.
from abc import ABC, abstractmethod
from os import access
class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

class BankAccount(Account):
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}.")
        else:
            print("Invalid deposit amount.")
                
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Account Holder: {self.account_holder}|")
        print(f"Current balance: {self._balance}")
    
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0):
        super().__init__(account_holder, initial_balance)

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0):
        super().__init__(account_holder, initial_balance)

account1 = SavingsAccount("Asim", 1000)
account2 = SavingsAccount("Sara", 2000)

print("\n---- Savings Account Operations --")
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()

print("\n---- Current Account Operations --")
account2.deposit(1000)
account2.withdraw(300)
account2.check_balance()