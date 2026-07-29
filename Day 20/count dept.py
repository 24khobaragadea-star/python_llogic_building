students = [
    ("Aarya", "CSE"),
    ("Rahul", "ECE"),
    ("Priya", "CSE"),
    ("Aman", "MECH"),
    ("Neha", "ECE"),
    ("Riya", "CSE")
]
group={}

for name,department in students:
    if department not in group:
        group[department]=1
    else:
        group[department]=group[department]+1
print(group)