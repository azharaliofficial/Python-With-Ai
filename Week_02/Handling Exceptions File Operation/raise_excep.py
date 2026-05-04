age = int(input("Enter your age: "))
if age<0:
    raise ValueError("Age is not negative")
else:
    print(f"age isn't negative")    