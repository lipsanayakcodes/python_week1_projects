# Mini Project (W1): 
# “Simple ATM Simulator”
# ● User login (PIN-based) 
# ● Options: check balance, deposit, withdraw
# ● Use functions for each operation 

def check_balance(balance):
    print("Your balance is:", balance)


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance = balance + amount
        print("Amount deposited successfully.")
        print("New balance:", balance)
    else:
        print("Invalid amount.")

    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance = balance - amount
        print("Please collect your cash.")
        print("Remaining balance:", balance)

    return balance


# PIN Login
correct_pin = "1234"
pin = input("Enter your PIN: ")

if pin == correct_pin:

    print("\nLogin successful!")
    print("Welcome to Simple ATM")

    balance = 5000

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit(balance)

        elif choice == "3":
            balance = withdraw(balance)

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN. Access denied.")