arr=[1,2,0,3,0,4,9]
new_arr=[]
zerocount=0

for num in arr:
    if num==0:
        zerocount=zerocount+1
    else:
        new_arr.append(num)

for i in range(zerocount):
    

     new_arr.append(0)
print(new_arr)

