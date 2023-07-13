import os

bank_data_file = "Bank Data.txt"
transaction_log_file = "Transaction Log.txt"

def read_balance():
    try:
        with open(bank_data_file, "r") as file:
            balance = float(file.read().strip())
            return balance
    except FileNotFoundError:
        return 0.0

def write_balance(balance):
    with open(bank_data_file, "w") as file:
        file.write(str(balance))

def log_transaction(transaction_type, amount):
    with open(transaction_log_file, "a") as file:
        file.write(f"{transaction_type}: {amount}\n")

def make_transaction():
    print("Would you like to make a transaction?")
    choice = input("Enter 'Yes' or 'No': ").lower()

    if choice == "yes":
        print("Would you like to make a deposit or withdrawal?")
        transaction_type = input("Enter 'deposit' or 'withdrawal': ").lower()

        if transaction_type == "deposit":
            amount = input("How much would you like to deposit? ")
            try:
                amount = float(amount)
                if amount > 0:
                    balance = read_balance()
                    balance += amount
                    write_balance(balance)
                    log_transaction("Deposit", amount)
                    print("Deposit successful.")
                else:
                    print("Invalid amount. Deposit amount must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif transaction_type == "withdrawal":
            amount = input("How much would you like to withdraw? ")
            try:
                amount = float(amount)
                balance = read_balance()
                if amount > 0 and balance >= amount:
                    balance -= amount
                    write_balance(balance)
                    log_transaction("Withdrawal", amount)
                    print("Withdrawal successful.")
                else:
                    print("Insufficient funds or invalid amount.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid transaction type.")
    elif choice == "no":
        print("No transaction requested.")
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

    print("Current balance:", read_balance())

make_transaction()
