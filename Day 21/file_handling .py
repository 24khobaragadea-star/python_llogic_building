

file=open("student.txt","r")
print(file.read())

file=open("student.txt","w")
file.write("marks are good , all passed ")
file.close()