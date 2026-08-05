students1 = [
    ("Aarya", 85),
    ("Rahul", 72),
    ("Priya", 91),
    ("Neha", 88)
]

file=open("students1.txt","w")
for name,marks in students1:
    file.write(name +"-" + str(marks)+ "\n")
file.close()

file=open("students1.txt","r")
print(file.read())
file.close()