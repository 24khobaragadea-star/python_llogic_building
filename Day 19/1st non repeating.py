employees = [
    "Aarya", "Rahul", "Priya", "Aarya",
    "Aman", "Rahul", "Aarya", "Priya",
    "Rahul", "Neha"
]
emp={}
for ch in employees:
    if ch not in emp:
        emp[ch]=1
    else:
        emp[ch]=emp[ch]+1
print(emp)

for student in employees:
    if emp[student]==1:
        print(student)
        break


