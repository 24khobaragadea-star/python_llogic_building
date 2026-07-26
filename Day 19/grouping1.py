products = [
    ("Laptop", "Electronics"),
    ("Shirt", "Clothing"),
    ("Phone", "Electronics"),
    ("Jeans", "Clothing"),
    ("Mouse", "Electronics")
]
group={}

for product,category in products:
    if category not in group:
        group[category]=[]

    group[category].append(product)

print(group)