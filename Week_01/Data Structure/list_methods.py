fruits = ["mango" , "orange" , "banana"]
print(fruits)

fruits.append("apple") #add item in last
print(fruits)

fruits.insert(0 , "grapes") #add item in index
print(fruits)

fruits.remove("banana") #remove item 
print(fruits)

fruits.pop() #remove last item
print(fruits)

fruits.sort() #sort list
print(fruits)

for fruit in fruits:
    print(fruit)
