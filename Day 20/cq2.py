students = [
    ("Aarya", "CSE", 85),
    ("Rahul", "ECE", 72),
    ("Priya", "CSE", 91),
    ("Aman", "MECH", 64),
    ("Neha", "ECE", 91),
    ("Riya", "CSE", 78),
    ("Karan", "MECH", 80)
]
high={}
for name,dept,marks in students:
    if dept not in high:
        high[dept]=marks
    elif marks>high[dept]:
        high[dept]=marks
for name,dept,marks in students:
    if marks==high[dept]:
        print(name,dept,marks)
      