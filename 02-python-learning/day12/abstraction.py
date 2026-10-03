class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Hidden - private
    
    def deposit(self, amount):  # Simple - hides SQL/validation
        self.__balance += amount

account = BankAccount(1000)
account.deposit(500)  # User doesn't know HOW it works