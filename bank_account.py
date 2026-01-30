# bank_account.py
# TASK 10: Object-Oriented Programming (OOP)

class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self._account_number = account_number
        self._holder_name = holder_name
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self._balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining Balance: ₹{self._balance}")
        else:
            print("Insufficient balance or invalid amount")

    def display_details(self):
        print("Account Number:", self._account_number)
        print("Account Holder:", self._holder_name)
        print("Balance: ₹", self._balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=4):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self._balance * self.interest_rate) / 100
        self._balance += interest
        print(f"Interest Added: ₹{interest}")
        print(f"Updated Balance: ₹{self._balance}")


# Creating objects
account1 = BankAccount("BA101", "Ravi", 5000)
account2 = SavingsAccount("SA201", "Anjali", 10000, 5)

# Simulating bank operations
print("\n--- Bank Account Operations ---")
account1.display_details()
account1.deposit(2000)
account1.withdraw(1500)

print("\n--- Savings Account Operations ---")
account2.display_details()
account2.deposit(3000)
account2.add_interest()
account2.withdraw(5000)
