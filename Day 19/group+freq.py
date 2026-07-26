orders = [
    ("Aarya", "Pizza"),
    ("Rahul", "Burger"),
    ("Aarya", "Burger"),
    ("Priya", "Pizza"),
    ("Aarya", "Pizza"),
    ("Rahul", "Pizza")
]
group={}

for name,order in orders:
    if name not in group :
        group[name]=1
    else:
        group[name]=group[name]+1


print(group)
