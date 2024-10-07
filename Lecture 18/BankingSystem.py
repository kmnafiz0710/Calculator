# Define all_account_number list globally outside the class to store all account numbers
all_account_numbers = []
accounts_list = []

class BankingSystem:
    def __init__(self, account_holder_name, account_number, initial_amount=0):
        # Ensure account number is unique
        if account_number in all_account_numbers:
            print("Account Number Already Exists. Enter a unique Account Number")
        else:
            # Append the new account number to the global list
            all_account_numbers.append(account_number)
            self.acc_holder_name = account_holder_name
            self.account_number = account_number
            self.total_amount = initial_amount
            accounts_list.append(self)
            print(f"\nHi, {self.acc_holder_name}!\n"
                  f"Your Account has been created.\n"
                  f"Your account number is {self.account_number}\n"
                  f"Remember your account number kindly.\n"
                  f"It wll be needed later\n"
                  f"Your Current Balance is {self.total_amount} tk.\n")

    def check_balance(self, account_number):
        # Check if the provided account number matches the stored one
        if account_number == self.account_number:
            print(f"Account Name: {self.acc_holder_name}")
            print(f"Your current balance: {self.total_amount} tk.")
        else:
            print("Enter a valid Account Number.")

    def deposit(self, account_number, amount):
        # Check if the account number is valid
        if account_number == self.account_number:
            if amount > 0:
                self.total_amount += amount
                print(f"{amount} tk have been deposited in account {self.account_number}.\n"
                      f"Your current balance is {self.total_amount} tk.")
            else:
                print(f"{amount} is not a valid amount to deposit.")
        else:
            print("Invalid account number.")

    def withdraw(self, account_number, amount):
        # Check if the account number is valid
        if account_number == self.account_number:
            if 0 < amount <= self.total_amount:
                self.total_amount -= amount
                print(f"{amount} tk withdrawn successfully from account {self.account_number}.\n"
                      f"Your current balance is {self.total_amount} tk.")
            else:
                print(f"Insufficient funds to withdraw {amount}.")
        else:
            print("Invalid account number.")

    def fund_transfer(self, sender_acc_num, recipient_acc_num, amount):
            if int(sender_acc_num) == self.account_number:
                if amount <= 0:
                    print("Invalid amount to transfer.")
                    return

                if self.total_amount >= amount:
                    recipient_account = None
                    for account in accounts_list:
                        if account.account_number == int(recipient_acc_num):
                            recipient_account = account
                            break

                    if recipient_account:
                        # Deduct from sender's account
                        self.total_amount -= amount
                        # Add to recipient's account
                        recipient_account.total_amount += amount
                        print(f"{amount} tk transferred to account number {recipient_acc_num}.\n"
                              f"Your current balance is {self.total_amount} tk.")
                    else:
                        print("Recipient account not found.")
                else:
                    print("Insufficient balance for the transfer.")
            else:
                print("Invalid sender account number.")



# Create accounts
account_1 = BankingSystem("Khaled Masud", 475, 1000)
account_2 = BankingSystem("Sumiya", 576, 2000)

# Deposit, Withdraw, Check Balance
print("\n")
account_1.deposit(475, 5000)
print("\n")
account_1.check_balance(475)
print("\n")
account_1.withdraw(475, 3000)
print("\n")
account_1.check_balance(475)

# Transfer Money
print("\nTransfer Money from Account 475 to 576:")
account_1.fund_transfer(475, 576, 1000)

# Check balances after transfer
print("\n")
account_1.check_balance(475)
account_2.check_balance(576)


