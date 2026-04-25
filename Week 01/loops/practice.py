num = int(input("Enter a Number: "))
count = 1
while count<=10:
    result = num*count
    print(f"{num}x{count} = {result}") #f is f-sting use for formatting
    count += 1

for r in range(1, 10):
    for c in range(r):
        print("*" , end="") #Sab kuch ek hi line mein jorne ke liye e.g ***
    print()    