arr=[4,8,7,9,2,1]

max1=8
max2=4

for num in arr[2:]:
    if num>max1:
        max2=max1
        max1=num
    elif max1>num>max2:
        max2=num
print("1st largest element : ",max1)
print("2nd largest element : ",max2)

## always remember hame jo update krna hota hai usko pehle likhte hai = ke 
## also we used slicing here , bcause we have to access element from out choice of position , not from start 
