# Use a single underscore (_) before a method name to indicate it is protected meant to be used within class or its subclasses.
# Use a double underscore (__) to define a private method accessible only within class due to name mangling.

class BankAccount:
    def __init__(self):
        self.balance=1000

    def _show_balance(self):
        print(f"balace is {self.balance}")

    def __update_balance(self,amt):
        self.balance+=amt

    def deposit(self,amt):
        if amt>0:
            self.__update_balance(amt)
            self._show_balance()

        else:
            print("invalid amount")

obj=BankAccount()
obj._show_balance()
obj.deposit(500)

