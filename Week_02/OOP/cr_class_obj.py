class Car:
    def drive(self):
        print("the car is moving")

car1 = Car()
car1.drive()

class Car:
    color = "red"
    def drive(self):
        print(f"{self.color} car is moving")

car1 = Car()
car1.drive()

class Car:
    color = "blue"
    def drive(self):
        print(f"{self.color} car is moving")
    def setColor(self , new_color):
        self.new_color = new_color
        print(f"{self.new_color} car is moving")    
        
car1 = Car()
car1.drive()
car1.setColor("green")        