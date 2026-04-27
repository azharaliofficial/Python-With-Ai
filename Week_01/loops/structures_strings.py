for char in "pakistan":
    print(char)

count = 0 
for character in "banana":
    # print(character)
    if character =="a":
        print(character)
        count +=1
print(count)

s = "python"
rev = "2"
for ch in s:
    print(ch)
    rev = ch + rev
print(rev)  


student  = {
    "name":"azhar ",
    "age":"34",
    "grade":"A"
}

for key in student:
    print(key)

student  = {
    "name":"azhar ",
    "age":"34",
    "grade":"A"
}

for key in student:
    print(student[key])

student  = {
    "name":"azhar ",
    "age":"34",
    "grade":"A"
}
for key in student:
    print(key , student[key])

student_list = [
    {
    "name":"azhar ",
    "age":"34",
    "grade":"A"
    },
    {
    "name":"ali",
    "age":"34",
    "grade":"B"
    }
]

for students in student_list:
    print(f"Name: {students.get('name' , '')} | Grade: {students.get('grade' , '')}")


