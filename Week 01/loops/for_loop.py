for i in range(3):
    print("this is print in 3  times")

for char in "pakistan":
    print(char)

i = 4 
rows = i
columns = i 

matrix= []
for r in range(rows):
    row=[]
    for c in range(columns):
        row.append(0)
        print(row)
    matrix.append(row)
for row in matrix:
        print(''.join(map(str , row)))

alphabets = ["A", "B" , "C" , "D"]
print(''.join(alphabets))   

rows = 6
for level in range (1 , rows + 1):
    # print(level)
    print(' ' * (rows - level) + '*' * (2 * level - 1))