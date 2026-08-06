file=open("emp.txt","a")
file.write("\nanurag")
file.close()

file=open("emp.txt","r")
print(file.read())
file.close()