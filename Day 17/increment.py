employees = [
    ["Aarya", 45000],
    ["Rahul", 28000],
    ["Priya", 60000],
    ["Aman", 35000]
]

for emp in employees:
    name=emp[0]
    salary=emp[1]
    if emp[1]<30000:
        emp[1]=emp[1]+5000
        

print(employees)