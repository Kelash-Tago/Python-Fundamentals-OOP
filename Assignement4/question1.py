class BankAccount:
    def __init__(self,accountNumber,ownerName,balance):
        self.accountNumber=accountNumber
        self.ownerName=ownerName
        self.balance=balance
    
    def deposit(self,amount):
        if(amount>0):
            self.balance+=amount
            print(amount," amount deposited succcessfully...")
        else:
            print("amount can not be deposited")
    def withdraw(self,amount):
        if(amount<self.balance):
            self.balance-=amount
            print(amount," amount withdrawl successfully...")
        else:
            print("Insufficient balance")
    def checkBalance(self):
        print("Your balance : ",self.balance)


kelash=BankAccount(1234,"Kelash",25000)
kelash.deposit(25000)
kelash.withdraw(10000)
kelash.checkBalance()

