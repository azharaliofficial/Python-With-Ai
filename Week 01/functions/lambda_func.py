add = lambda a,b: a+b
print(add(6,7))

double_it = lambda num: num*2
print(double_it(5))

nums = [1, 2, 3, 4]
squares = list(map(lambda  x : x*x , nums))
print(squares)

num = [ 1, 3, 4 ,5 ,7, 8 ,9 ,10, 11]
odd_numbers = list(filter(lambda x : x%2 !=0 , num))
print(odd_numbers)