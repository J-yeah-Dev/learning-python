class BankAccount:
    def __init__(self, owner_name, initial_balance=0.0):
        self.owner = owner_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount:.2f}. New Balance: ₹{self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print(f"Declined! Insufficient funds. Balance: ₹{self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount:.2f}. Remaining Balance: ₹{self.balance:.2f}")

    def display_balance(self):
        print(f"\n--- Account Holder: {self.owner} | Balance: ₹{self.balance:.2f} ---")


print("=== Welcome to the Terminal Bank ===")
name = input("Enter your name to open an account: ")
account = BankAccount(name)

while True:
    account.display_balance()
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Exit System")
    
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        amount = float(input("Enter deposit amount: ₹"))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: ₹"))
        account.withdraw(amount)
    elif choice == "3":
        print(f"\nThank you for banking with us, {account.owner}! Goodbye.")
        break
    else:
        print("Invalid choice. Please pick 1, 2, or 3.")
