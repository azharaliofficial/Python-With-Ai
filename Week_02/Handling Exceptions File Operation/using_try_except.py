# num = int(input("Enter a number"))
# print(num/0)

try:
    num  = int(input("Enter a number: "))
    result = 10/num
    print("Running code....")
except ZeroDivisionError:
    print("you cann't be divide by zero")
except ValueError:
    print("this is not a number")        
except Exception as e:
    print(f"An unexpected error : {e}")    
else:
    print("Success! no error")    
finally:
    print("Done!")    


