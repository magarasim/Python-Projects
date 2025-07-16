balance = 10000  # Initial balance
pin = 1234  # Default PIN

if balance <= 0:
    print("Insufficient balance.")
pin_input = int(input("Enter your PIN: "))
if pin_input == pin:
    print(f"Your current balance is: ${balance}")
    choice = input("enter 'withdraw' to withdraw money or 'exit' to exit: ").lower()
    if choice == 'withdraw':
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful! New balance: ${balance}")
        else:
            print("Insufficient funds for this withdrawal.")
else:
    print("Incorrect PIN. Access denied.")