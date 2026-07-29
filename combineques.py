students = [
    ("Aarya", 85),
    ("Rahul", 72),
    ("Priya", 91),
    ("Aman", 64),
    ("Neha", 91),
    ("Riya", 78)
]

highest=0

for name , marks in students:
    if marks>highest:
        highest=marks
print(highest)
for name,marks in students:
    if marks==highest:
        print(name)
