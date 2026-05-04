# with open("missing.txt" , "r") as file:
    # print(file.read()) #Error

try:
    with open("missing.txt" , "r") as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")    

fileName = "Week_02/Handling Exceptions File Operation/my_info.txt"
name = "Azhar ali"
age = 20
try:
    with open(fileName , "r") as fin:
        print(fin.read())
except FileNotFoundError:
    with open(fileName , "w") as fout:
        fout.write(f"{name}\n{age}")        
    with open(fileName , "r") as fin:
        print(fin.read())   

       