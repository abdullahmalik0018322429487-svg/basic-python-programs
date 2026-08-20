# Initial balance
balance = 15000

# User se withdrawal amount input lein
amount = int(input("Enter withdrawal amount: "))

# Balance check
if amount <= balance:
    balance = balance - amount
    print("Transaction Successful!")
    print("Updated Balance:", balance)
else:
    print("Insufficient Funds")