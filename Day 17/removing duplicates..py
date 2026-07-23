employees = [
    ["Aarya", "CSE"],
    ["Rahul", "ECE"],
    ["Aarya", "CSE"],
    ["Priya", "CSE"],
    ["Rahul", "ECE"],
    ["Neha", "MECH"]
]
result=[]

for emp in employees:
    name=emp[0]
    dept=emp[1]

    if emp not in result :
        result.append(emp)
    
print(result)
