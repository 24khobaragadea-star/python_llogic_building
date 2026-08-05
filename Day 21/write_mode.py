students = [
    "Aarya",
    "Rahul",
    "Priya",
    "Neha",
    "Aarav"
]

file=open("students.txt","w")

for stud in students:
    file.write(stud +"\n")
file.close()