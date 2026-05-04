class Dog:
    def __init__(self):
        self.name = "buddy"
    def bark(self):
        print(f"{self.name} says Woof!")
dog1 = Dog()        
dog1.bark()

class Car:
    def __init__(self , brand , color):
        self.brand = brand
        self.color = color

car1 = Car("toyota" , "red")        
print(car1.brand)
print(car1.color)
car1.color = "blue"
print(car1.color)

car2 = Car("Honda" , "green")
print(car2.brand)
print(car2.color)

