class invalidAge(Exception):
    pass
fileName = "Week_02/Handling Exceptions File Operation/user_data.txt"

try:
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    user_city = input("Enter your city name: ")

    if user_age<0:
        raise invalidAge(f"The age isn't negative : {user_age}") 

    try:

        with open(fileName , "a") as append:
            append.write(f"Name:{user_name}\nAge:{user_age}\nCity:{user_city}\n\n")
        with open(fileName , "r") as fin:
            fin.read()   

    except FileNotFoundError:
        with open(fileName , "w") as fout:
            fout.write(f"Name:{user_name}\nAge:{user_age}\nCity:{user_city}\n\n")
        with open(fileName , "r") as fin:
            fin.read()    

except ValueError:
    print("Invalid credentinals!")        
finally:
    print("Done!")    