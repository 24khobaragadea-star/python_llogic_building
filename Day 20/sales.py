sales = [
    ("Aarya", "Electronics", 50000),
    ("Rahul", "Clothing", 30000),
    ("Priya", "Electronics", 70000),
    ("Aman", "Clothing", 45000),
    ("Neha", "Electronics", 60000),
    ("Riya", "Clothing", 45000)
]
highest={}
for name,category,sale in sales:
    if category not in highest:
        highest[category]=sale
    elif sale>highest[category]:
        highest[category]  =sale

for name,category,sale in sales:
    if sale==highest[category]:
        print(name,category,sale)  