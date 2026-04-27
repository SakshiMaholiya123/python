def decorator(fun):
    def wrapper():
        print("before")
        fun()
        print("after")
    return wrapper
    
@decorator
def greet():
    print("hello0")

greet()

