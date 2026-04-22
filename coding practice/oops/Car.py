# Create a Car class
# brand, speed
# method: increase_speed(value)
class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    
    def increase_speed(self,speed_value):
        self.speed+=speed_value

    
    def updated_speed(self):
        return self.speed

car=Car("Audi",80)
car.increase_speed(20)

print(f" updated speed is {car.updated_speed()}")
        