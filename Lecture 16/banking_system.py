class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Name of the account holder
        self.balance = initial_balance          # Initial balance of the account

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}."
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def get_balance(self):
        return f"Current balance: ${self.balance}."


# Example usage:
account = BankAccount("Alice", 100)  # Creating an account for Alice with an initial balance of $100
print(account.get_balance())          # Output: Current balance: $100.
print(account.deposit(50))             # Output: Deposited $50. New balance: $150.
print(account.withdraw(30))            # Output: Withdrew $30. New balance: $120.
print(account.withdraw(200))           # Output: Insufficient funds.
print(account.get_balance())          # Output: Current balance: $120.



# ---------
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}."
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def get_balance(self):
        return f"Current balance: ${self.balance}."


# Main program
if __name__ == "__main__":
    account_holder = input("Enter the account holder's name: ")
    initial_balance = float(input("Enter the initial balance (default is $0): ") or 0)

    account = BankAccount(account_holder, initial_balance)

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            print(account.deposit(amount))
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            print(account.withdraw(amount))
        elif choice == '3':
            print(account.get_balance())
        elif choice == '4':
            print("Exiting the banking system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
