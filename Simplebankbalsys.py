balance = 1000   # global variable

def deposit(amount):
     global balance
     balance += amount
     print("Balance after deposit:", balance)

def withdraw(amount):
     global balance
     balance -= amount
     print("Balance after withdrawal:", balance)

#function calls
deposit(500)
withdraw(300)