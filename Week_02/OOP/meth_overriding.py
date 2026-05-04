class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof Woof!")

dog1 = Dog()        
dog1.speak()
