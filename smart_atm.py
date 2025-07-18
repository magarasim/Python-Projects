pin = 1234
attempt = 0
while attempt < 2:
    entered_pin = int(input("Enter your PIN: "))
    if entered_pin == pin:
        print("Access granted.")
        break
    else:
        print("Incorrect PIN. Please try again.")
        attempt += 1
else:
    print("Access Blocked. Too many incorrect attempts.")