def sum(a , b):
        result = a+b
        return result

cube = lambda x : x*x*x

def main():
        a = float(input("Enter a num:"))
        b = float(input("enter a num:"))
        total_sum = sum(a , b)
        print("the result is :" , total_sum)

        cube_number = float(input("enter a num for cube:"))
        result = cube(cube_number)
        print("the cube is " , result)

main()