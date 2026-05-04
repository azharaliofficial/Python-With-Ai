class Student:
    def __init__(self , name , grade):
        self.__grade= grade
student1 = Student("Ali" , 90)        
# print(student1.__grade) #Error

class Student:
    def __init__(self , grade):
        self.__grade = grade
    def getGrade(self):
        return self.__grade

student1 = Student(90)         
print(student1.getGrade())

class Student:
    @property
    def grade(self):
        return self.__grade
    
    def __init__(self , grade):
        self.__grade = grade
    def getGrade(self):
        return self.__grade
    def setGrade(self , grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("invalid grade!")

student1 = Student(55)
print(student1.getGrade())  
student1.setGrade(-3)
print(student1.grade)  

          