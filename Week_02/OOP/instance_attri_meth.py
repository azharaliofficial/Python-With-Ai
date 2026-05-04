class Student:
    def __init__(self , name , age , grade):
        self.name = name
        self.age = age
        self.grade = grade
    def display_info(self):
        print(f"Student Name : {self.name}")    
        print(f"Student Age : {self.age}")    
        print(f"Student Grade : {self.grade}")    
    def is_eligible(self):
        if self.grade >= 80:
            print(f"{self.name} is eligible for scholarship") 
        else:
            print(f"{self.name} is not eligible") 
Student1 = Student("Azhar" , 20 , 70)
Student1.display_info()  
Student1.is_eligible()                