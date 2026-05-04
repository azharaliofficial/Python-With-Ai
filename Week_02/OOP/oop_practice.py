class Car:
    def __init__(self , color):
        self.color = color

    def start(self):
        print(f"{self.color} car started")    

my_car = Car("red")
my_car.start()        

mybrother_car = Car("Blue")
mybrother_car.start()