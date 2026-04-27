from abc import ABC,abstractmethod

def transaction_logger(fun):
    def wrapper(self,amount):
        print("before transaction")
        res=fun(self,amount)
        print("after transaction")
        return res
    return wrapper

class Account(ABC):
    def __init__(self,account_number,__balance):
        self.account_number=account_number
        self.__balance=__balance

    @transaction_logger
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("deposited",amount)

        else:
            print("invalid amount")

    @abstractmethod
    def withdraw(self,amount):
        pass

    @property
    def balance(self):
            return self.__balance
    
    def update_balance(self,amount):
        self.__balance+=amount

    def __str__(self):
        return f"account number is {self.account_number} and balance is {self.balance}" 

class SavingsAccount(Account):
    def __init__(self, account_number, __balance):
        super().__init__(account_number, __balance)

    @transaction_logger
    def withdraw(self,amount):
        if self.balance-amount<500:
            print("Cannot withdraw")
        else:
            self.update_balance(-amount)
            print("withdraw",amount)

class CurrentAccount(Account):
    def __init__(self, account_number, __balance):
        super().__init__(account_number, __balance)
    
    @transaction_logger
    def withdraw(self,amount):
        if self.balance-amount<-1000:
            print("Cannot withdraw")
        else:
            self.update_balance(-amount)
            print("withdraw",amount)

class Customer:
    def __init__(self,name,account):
        self.name=name
        self.account=account

    def details(self,name,account):
        print(f"name is {self.name} and account is {self.account}")

acc = SavingsAccount("101", 1000)
acc.deposit(500)
acc.withdraw(700)
print(acc)


        