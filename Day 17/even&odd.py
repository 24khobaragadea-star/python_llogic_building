numbers = [12, 5, 8, 21, 16, 3, 10, 7]
even=[]
odd=[]

for num in numbers:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)

print("even : ",even)
print("odd : ",odd)