my_set = {1, 2 ,2, 3, 4, 5} #sets are unique thats why duplicated items aren't show
print(my_set)

my_set.add(6)
my_set.remove(1)
print(my_set)

#set operations
A = {1, 2, 3, 4}
B = {4, 5, 6, 7}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
