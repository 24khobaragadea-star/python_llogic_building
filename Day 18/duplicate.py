numbers = [10, 20, 30, 10, 20, 10, 40]
seen={}
for num in numbers:
    if num not in seen:
        seen[num]=1
    else:
        seen[num]=seen[num]+1
print(seen)

for number,count in seen.items():
    if count>1:
        print(number)

