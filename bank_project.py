class Bank_Account:
    def __init__(self):
        self.balance = 0

    def deep(self):
        print("Press 1 for Deposite Money")
        print("Press 2 for Withdraw Money")

    def deposit(self):
        self.amount = float(input("Enter amount to be Deposited : "))
        self.balance += self.amount
        print("Amount Deposited:",'Rs.',self.amount)
        print('Your Balance is :','Rs.',self.balance)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn : "))
        if self.balance >= amount:
            self.balance -= amount
            print("You have Withdrawn :",'Rs.',amount)
        else:
            print("U have Insufficient Balance  ")

    def display(self):
        print("Net Available Balance :",'Rs.',self.balance)

print("Hello!!! Welcome to the Soni Bank")
s = Bank_Account()
s.deep()
choice=int(input("Enter Here Your Choice :"))
if choice is 1:
    s.deposit()
    c=input('Do u want Another Transaction Y or N :')
    if c is 'y':
        s.deep()
        choice = int(input("Enter Here Your Choice :"))
        if choice is 1:
            s.deposit()
        elif choice is 2:
            s.withdraw()
            s.display()
        else:
            print("invalid")
    else:
        print('THANKS FOR CHOOSING OUR BANK')
elif choice is 2:
    s.withdraw()
    s.display()
else:
    print("Invalid Choice")