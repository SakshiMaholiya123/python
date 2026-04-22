class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    
    def deposit(self,amt):
        self.balance+=amt

    def get_balance(self):
        print(f"balance {self.balance}")

acc=BankAccount(100)
acc.get_balance() 

acc.deposit(50)  #add the amt into balance

acc.get_balance()