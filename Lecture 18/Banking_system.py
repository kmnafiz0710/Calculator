class BankingSystem:
    def __init__(self, account_holder_name, initial_amount=0):
        self.acc_holder_name = account_holder_name
        self.total_amount = initial_amount
        self.deposit_by = None
        self.withdraw_by = None
        print(f"Hi, {self.acc_holder_name}!\n Your Account has been created. \n Your Current Balance is {self.total_amount}")

    def check_balance(self):
        print(f"Account Name: {self.acc_holder_name}")
        print(f"Your current balance: {self.total_amount}")

    def deposit(self,name, amount):
        self.deposit_by = name
        if amount > 0:
            self.total_amount += amount
            print(f"{amount} tk deposited by {self.deposit_by}.")
        else:
            print(f"{amount} is not valid amount to deposit.")

    def withdraw(self,name, amount):
        self.withdraw_by = name
        if 0 < amount <= self.total_amount:
            self.total_amount -= amount
            print(f"{amount} tk withdraw by {self.withdraw_by}.")
        else:
            print(f"Insufficient funds to withdraw {amount}.\n {amount} is not valid amount to withdraw.")


# Name= input("Enter Your Name: ")
# Init_Balance= int(input("Enter Your Initial Amount: "))
Account_1 = BankingSystem("Khaled Masud", 1000)

Account_1.check_balance()
Account_1.deposit("Khaled", 5000)
Account_1.check_balance()
Account_1.withdraw("Khaled Masud", 3000)
Account_1.check_balance()
Account_1.withdraw("Khaled Masud", 5000)

