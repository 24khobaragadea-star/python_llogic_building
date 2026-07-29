students = [
    "Aarya", "Rahul", "Priya", "Aarya",
    "Aman", "Rahul", "Neha", "Priya",
    "Aarya"
]
seen=set()
duplicates=set()
for ch in students:
    if ch not in seen:
        seen.add(ch)
    else:
        duplicates.add(ch)
print(seen)
print(duplicates)
