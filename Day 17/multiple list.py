employees = [
    ["Aarya", 45000, "CSE"],
    ["Rahul", 28000, "ECE"],
    ["Priya", 60000, "CSE"],
    ["Aman", 35000, "MECH"],
    ["Neha", 75000, "CSE"]
]
result=[]
for employee in employees:
    name=employee[0]
    salary=employee[1]
    dept=employee[2]

    if salary > 40000 and dept=="CSE":
        result.append(name)

print(result)
