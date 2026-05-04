file = open("Week_02/Read and Write files/demo.txt" , "r")
print(file.read())
file.close()

file = open("Week_02/Read and Write files/demo.txt" , "w")
file.write("this text is  write in demo file")
file.close()

file = open("Week_02/Read and Write files/demo.txt" , "a")
file.write("\nnew line is added")
file.close()