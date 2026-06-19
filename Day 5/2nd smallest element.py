arr=[8,4,2,3,1,5]

min1=4
min2=8

for num in arr[2:]:
    if num < min1:
        
        min2=min1     # always remember the order 
        min1=num
    elif min1<num<min2:
        min2=num
print(min1)
print(min2)