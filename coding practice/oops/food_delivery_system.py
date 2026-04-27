from abc import ABC,abstractmethod

def order_logger(fun):
    def wrapper(self,*args,**kwargs):
        print("order started")
        res=fun(self,*args,**kwargs)
        print("order completed")
        return res
        
    return wrapper
        
class User(ABC):
    def __init__(self,name,location):
        self.name=name
        self.location=location

    def show_details(self):
        print(f"name is {self.name} and location is {self.location}")

    @abstractmethod
    def place_order(self,*args):
        pass
        
class Customer(User):
    def __init__(self, name, location):
        super().__init__(name, location)

    @order_logger
    def place_order(self,restaurant,item):
        return Order(self,restaurant,item)

class DeliveryPartner(User):
    def __init__(self, name, location):
        super().__init__(name, location)

    def place_order(self,*args,**kwargs):
        print("cant place order")

class Restaurant:
    def __init__(self,name):
        self.name=name
        self.__menu={}
    def add_item(self, item,price):
        self.__menu[item]=price

    def show_menu(self):
        for item,price in __menu.items():
            print(item ,":", price)

class Order:
    def __init__(self,customer,restaurant,items):
        self.customer=customer
        self.restaurant=restaurant
        self.items=items

    def __str__(self):
        return f"customer name is {self.customer.name} ,restraunt is {self.restaurant.name} and items {self.items} "

r = Restaurant("Pizza Hut")
r.add_item("Pizza", 300)
r.add_item("Burger", 150)

c = Customer("Sakshi", "Delhi")
order = c.place_order(r, ["Pizza", "Burger"])

print(order)


