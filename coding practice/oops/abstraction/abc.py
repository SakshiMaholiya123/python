from abc import ABC,abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass

class English(Greet):
    def say_hello(self):
        print("hello")

obj=English()
obj.say_hello()