class Animal:
    def speak(self):
        print("some sound")

class Dog(Animal):
    pass

dog1 = Dog()
dog1.speak()

class Dog(Animal):
    def bark(self):
        print("Woof!")

child_dog = Dog()
child_dog.speak()        
child_dog.bark()        