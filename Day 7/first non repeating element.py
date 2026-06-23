arr=[1,1,2,2,3,3,3,4]
count=0

for num in arr:
    count = 0

    for x in arr:
        if x==num:
            count=count+1
    if count==1:
        print(num)
        break

