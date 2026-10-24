class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Please enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully!")

    def check_balance(self):
        print("Current Balance:", self.balance)


# Create a bank account
account = BankAccount("12345", "Prema", 1000)

print("Welcome,", account.account_holder)

# Menu-driven program
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Please try again.")