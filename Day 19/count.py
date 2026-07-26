employees = [
    "Aarya", "Rahul", "Priya", "Aarya",
    "Aman", "Rahul", "Aarya", "Priya",
    "Rahul", "Neha"
]
emp1={}
max=0


for ch in employees:
    if ch not in emp1:
        emp1[ch]=1
    else:
        emp1[ch]=emp1[ch]+1

print(emp1)
for student,count in emp1.items():
    if count>max:
        max=count
print(max)

for students,count in emp1.items():
    if max==count:
        print(students)


    