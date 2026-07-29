# ============================================================
# 1. COUNT NUMBER OF STUDENTS IN EACH DEPARTMENT
# ============================================================

students = [
    ("Aarya", "CSE"),
    ("Rahul", "ECE"),
    ("Priya", "CSE"),
    ("Aman", "MECH"),
    ("Neha", "ECE"),
    ("Riya", "CSE")
]

group = {}

for name, department in students:
    if department not in group:
        group[department] = 1
    else:
        group[department] = group[department] + 1

print(group)


# ============================================================
# 2. FIND HIGHEST PAID EMPLOYEE IN IT DEPARTMENT
# ============================================================

employees = [
    ("Aarya", 55000, "IT"),
    ("Rahul", 70000, "HR"),
    ("Priya", 70000, "IT"),
    ("Aman", 45000, "Sales"),
    ("Neha", 60000, "IT")
]

high = 0

for name, salary, dept in employees:
    if dept == "IT":
        if salary > high:
            high = salary

for name, salary, dept in employees:
    if dept == "IT" and salary == high:
        print(name, salary)


# ============================================================
# 3. FIND TOP SCORER FROM EACH DEPARTMENT
# ============================================================

students = [
    ("Aarya", "CSE", 85),
    ("Rahul", "ECE", 72),
    ("Priya", "CSE", 91),
    ("Aman", "MECH", 64),
    ("Neha", "ECE", 91),
    ("Riya", "CSE", 78),
    ("Karan", "MECH", 80)
]

high = {}

for name, dept, marks in students:
    if dept not in high:
        high[dept] = marks
    elif marks > high[dept]:
        high[dept] = marks

for name, dept, marks in students:
    if marks == high[dept]:
        print(name, dept, marks)


# ============================================================
# 4. FIND UNION AND DIFFERENCE OF TWO LISTS
# ============================================================

list1 = [10, 20, 30, 40, 50, 60]
list2 = [20, 40, 60, 80, 100]

result = set(list1) | set(list2)
print(result)

result1 = set(list1) - set(list2)
result2 = set(list2) - set(list1)

print(result1)
print(result2)


# ============================================================
# 5. FIND HIGHEST SALE FROM EACH CATEGORY
# ============================================================

sales = [
    ("Aarya", "Electronics", 50000),
    ("Rahul", "Clothing", 30000),
    ("Priya", "Electronics", 70000),
    ("Aman", "Clothing", 45000),
    ("Neha", "Electronics", 60000),
    ("Riya", "Clothing", 45000)
]

highest = {}

for name, category, sale in sales:
    if category not in highest:
        highest[category] = sale
    elif sale > highest[category]:
        highest[category] = sale

for name, category, sale in sales:
    if sale == highest[category]:
        print(name, category, sale)


# ============================================================
# 6. FIND DUPLICATE STUDENT NAMES
# ============================================================

students = [
    "Aarya", "Rahul", "Priya", "Aarya",
    "Aman", "Rahul", "Neha", "Priya",
    "Aarya"
]

seen = set()
duplicates = set()

for ch in students:
    if ch not in seen:
        seen.add(ch)
    else:
        duplicates.add(ch)

print(seen)
print(duplicates)


# ============================================================
# 7. FIND HIGHEST MARKS AND STUDENT(S) WHO SCORED THEM
# ============================================================

students = [
    ("Aarya", 85),
    ("Rahul", 72),
    ("Priya", 91),
    ("Aman", 64),
    ("Neha", 91),
    ("Riya", 78)
]

highest = 0

for name, marks in students:
    if marks > highest:
        highest = marks

print(highest)

for name, marks in students:
    if marks == highest:
        print(name)