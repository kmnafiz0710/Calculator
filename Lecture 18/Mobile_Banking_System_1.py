import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",  # Default XAMPP username is 'root'
    password="",  # Default XAMPP has an empty password
    database="mobile_banking"
)
cursor = connection.cursor()


# Mobile Banking system like Nagad
all_account_numbers = []

# Banking System class
class BankingSystem:
    def __init__(self, account_holder_name, account_number, pin_number, initial_amount=0):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mobile_banking"
        )
        cursor = connection.cursor()

        # Check if account already exists in the database
        cursor.execute("SELECT account_number FROM accounts WHERE account_number = %s", (account_number,))
        existing_account = cursor.fetchone()

        if existing_account:
            print("Account Number Already Exists. Enter a unique Account Number")
        else:
            # Add new account to the database
            cursor.execute(
                "INSERT INTO accounts (account_holder_name, account_number, pin_number, total_amount) VALUES (%s, %s, %s, %s)",
                (account_holder_name, account_number, pin_number, initial_amount))
            connection.commit()
            print(f"\nHi, {self.acc_holder_name}!\nYour Account has been created.\n"
                  f"Your Current Balance is {self.total_amount} tk.\n"
                  f"Your account number is {self.account_number}\n"
                  f"Your pin number is {self.pin_number}\n"
                  f"Don't share your PIN number with anyone.")
        cursor.close()
        connection.close()

    def check_balance(self, pin_number):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mobile_banking"
        )
        cursor = connection.cursor()

        cursor.execute(
            "SELECT total_amount, account_holder_name FROM accounts WHERE account_number = %s AND pin_number = %s",
            (self.account_number, pin_number))
        account_data = cursor.fetchone()

        if account_data:
            print(f"\nAccount Name: {account_data[1]}")
            print(f"Your current balance: {account_data[0]} tk.")
        else:
            print("\nInvalid Pin Number")

        cursor.close()
        connection.close()

    def deposit(self, amount, pin_number):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mobile_banking"
        )
        cursor = connection.cursor()

        # Check if the PIN is correct
        cursor.execute("SELECT total_amount FROM accounts WHERE account_number = %s AND pin_number = %s",
                       (self.account_number, pin_number))
        account_data = cursor.fetchone()

        if account_data:
            if amount > 0:
                new_balance = account_data[0] + amount
                cursor.execute("UPDATE accounts SET total_amount = %s WHERE account_number = %s",
                               (new_balance, self.account_number))
                connection.commit()
                print(f"\n{amount} tk have been deposited.\nYour Current Balance is {new_balance} tk.")
            else:
                print(f"\n{amount} is not a valid amount to deposit.")
        else:
            print("\nInvalid Pin Number")

        cursor.close()
        connection.close()

    def withdraw(self, amount, pin_number):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mobile_banking"
        )
        cursor = connection.cursor()

        # Check if the PIN is correct and balance is sufficient
        cursor.execute("SELECT total_amount FROM accounts WHERE account_number = %s AND pin_number = %s",
                       (self.account_number, pin_number))
        account_data = cursor.fetchone()

        if account_data:
            if 0 < amount <= account_data[0]:
                new_balance = account_data[0] - amount
                cursor.execute("UPDATE accounts SET total_amount = %s WHERE account_number = %s",
                               (new_balance, self.account_number))
                connection.commit()
                print(f"\n{amount} tk withdrawn successfully.\nYour Current Balance is {new_balance} tk.")
            else:
                print(f"\nInsufficient funds to withdraw {amount} tk.")
        else:
            print("\nInvalid Pin Number")

        cursor.close()
        connection.close()



    def account_info(self,pin_number):
        if int(pin_number)==self.pin_number:
            print(f"\nAccount holder name: {self.acc_holder_name}.\n"
                  f"Your account number is {self.account_number}\n"
                  f"Your Current Balance is {self.total_amount} tk.\n"
                  f"Your pin number is {self.pin_number}\n"
                  f"Don't share your PIN number with anyone.")


def show_menu():
    account = None

    while True:
        # Displaying menu options
        menu = ("\n"
                "1. Create Account\n"
                "2. Deposit\n"
                "3. Withdraw\n"
                "4. Check Balance\n"
                "5. Account Details\n"
                "6. Exit")
        print(menu)

        # Get user input
        choice = input("Enter your choice (1-5): ")

        # Perform actions based on user choice
        if choice == "1":
            # Create account
            print("\n")
            name = input("Enter your name: ")
            acc_num = int(input("Enter account number: "))
            pin_number = int(input("Enter your pin number: "))
            initial_amount = int(input("Enter initial amount: "))
            account = BankingSystem(name, acc_num,pin_number, initial_amount)

        elif choice == "2":
            if account is None:
                print("\nYou have no account.\n"
                      "Please create an account first.")
            else:
                # Deposit money
                amount = float(input("Enter amount to deposit: "))
                pin_number = int(input("Enter your pin number: "))
                account.deposit(amount,pin_number)

        elif choice == "3":
            if account is None:
                print("\nYou have no account.\n"
                      "Please create an account first.")
            else:
                # Withdraw money
                amount = float(input("Enter amount to withdraw: "))
                pin_number = input("Enter your pin number: ")
                account.withdraw(amount,pin_number)

        elif choice == "4":
            if account is None:
                print("\nYou have no account.\n"
                      "Please create an account first.")
            else:
                # Check balance
                pin_number = input("Enter your pin number: ")
                account.check_balance(pin_number)

        elif choice == "5":
            if account is None:
                print("\nYou have no account.\n")
                print("Please create an account first.")
            else:
                pin_number = input("Enter your pin number: ")
                account.account_info(pin_number)

        elif choice == "6":
            # Exit the program
            print("\nThank you for banking with us.")
            break

        else:
            print("\nInvalid choice. Please choose between 1 to 5.")

# Start the program
# show_menu()
print("To open menu, Enter *167# code.")
while True:
    mobile_menu=input("Enter code: ")
    if mobile_menu == "*167#":
        print("Welcome to Nagad.")
        show_menu()
    else:
        print("Invalid choice. Please choose *167# code.")
