for outer in range(3):
    print(outer)
    print("outer loop")
    for inner in range(3):
        print(inner)
        print("inner loop")

i  = 4 
row = i
col = i 

matrix = []

for r in range(row):
    rows = []
    for c in range(col):
        rows.append(0)
        print(rows)
    matrix.append(rows)
    print(matrix)
for rows in matrix:
    print(''.join(map(str , rows)))
