arr=[9,6,5,4,3,2]

last=arr[len(arr)-1]

for num in range(len(arr)-2,-1,-1):
    arr[num+1]=arr[num]
arr[0]=last
print(arr)

