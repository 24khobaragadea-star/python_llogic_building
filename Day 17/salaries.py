names = ["Aarya", "Rahul", "Priya", "Aman", "Neha"]
salaries = [25000, 45000, 18000, 60000, 32000]
result=[]

for index in range(len(names)):
    if salaries[index]>30000:
        result.append(names[index])

print(result)