class Bank:
    bank_name="ICIC"
    
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
           print("Insufficient Balance")
        else:
            self.balance -= amount
            
    def display_balance(self):
        print(self.balance)

account = Bank(1526,5000)
account.deposit(1000)
account.withdraw(4000)
account.display_balance()
