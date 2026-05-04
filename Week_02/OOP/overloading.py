class Calculator:
    def add(self , a , b=0 , c=0):
        return a + b + c
calc1 = Calculator()
print(calc1.add(5))   
print(calc1.add(5 ,10 ,30))