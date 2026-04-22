# Counter Class
# starts from 0
# has method increment()
# prints current count

class Counter:
    # def current_counter(self,counter):
    #     self.counter=counter
 
    
    def __init__(self,counter):
        self.counter=counter
        
    def updated_counter(self,increment=1):
         self.counter+=increment

    def display(self):
        return self.increment
obj=Counter(2)
print(f"updated counter is {obj.updated_counter()}")