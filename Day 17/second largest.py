numbers=[10, 50, 20, 30, 40]

max1=numbers[0]
max2=numbers[1]

for num in numbers:
    if num > max1 :
        max2=max1
        max1=num
    elif max1>num>max2:
        max2=num
print(max2)
print(max1)
        