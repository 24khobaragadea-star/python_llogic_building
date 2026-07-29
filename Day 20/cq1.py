employees = [
    ("Aarya", 55000, "IT"),
    ("Rahul", 70000, "HR"),
    ("Priya", 70000, "IT"),
    ("Aman", 45000, "Sales"),
    ("Neha", 60000, "IT")
]
high=0

for name,salary,dept in employees:
    if dept=="IT":
        if salary>high:
            high=salary

for name,salary,dept in employees:
    if dept=="IT" and salary==high:
        print(name,salary)
