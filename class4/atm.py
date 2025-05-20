
def check_my_balance(balance):
    print(f"Your balance is {balance}")
    return balance

def withdraw(amount, balance):
    if amount > balance:
        # give an error saying that balance is less
        # balance = balance + amount
        raise ValueError("Insufficient Balance")

    if amount < 10:
        raise ValueError("At least 10$ should be withdrawn")

    balance = balance - amount
    print(f"Thanks for withdrawing {amount}")
    return balance


def deposit(amount, balance):
    if amount > 20000:
        raise ValueError("You can't deposit more than 20,000$")

    # balance = balance + amount
    balance += amount # balance = balance + amount
    print(f"You deposited {amount}")
    return balance


balance = 1000
while True:
    choice = input("What do you want to do?")
    choice = int(choice)
    
    if choice == 1:
        balance = check_my_balance(balance)
    
    elif choice == 4:
        print("You exited ATM")
        break
    
    elif choice == 2:
        amount = input("Please Type your amount: ")
        print(f"Are you sure you want to deposit {amount}?")
        yes_or_no = input("Type yes or no: ")
    
        if yes_or_no == "yes" or yes_or_no == "y":
            balance = deposit(int(amount), balance)
            print(f"Your new Balance: {balance}")

        else:
            continue

    elif choice == 3:
        amount = input("Please Type your amount: ")
        balance = withdraw(int(amount), balance)
        print(f"Your new Balance: {balance}")

    else:
        print("Error: Type between 1 to 4")
    

# Transaction History # list
