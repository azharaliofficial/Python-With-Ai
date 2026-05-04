class InvalidAgeError(Exception):
    pass

age = int(input("Enter age: "))
if age<0:
    raise InvalidAgeError(f"age cann't be negative!, {age}")

try:
    age = int(input("Enterage: "))
    if age<0:
        raise InvalidAgeError(f"Age cann't be negative , {age}")

except InvalidAgeError as e:
    print(e)        