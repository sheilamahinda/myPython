class BankAccount:
    def __init__(self, account_number, holder_name, account_balance = 0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_balance = account_balance
    def deposit(self, amount):
        self.account_balance +=amount
    def withdraw(self, amount):
        if self.account_balance >= amount:
           self.account_balance -= amount
        else:
            print("Insufficient funds")
    def display_account_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Account Balance: {self.account_balance}")

my_account=BankAccount("123456789", "Erick", 1000)
my_account.display_account_balance()
my_account.deposit(500)
my_account.display_account_balance()
my_account.withdraw(2000)
