arr=[1,2,3,4,5]
reverse_arr=[]

index=len(arr)-1

for num in arr:
    reverse_arr.append(arr[index])
    index=index-1

print(arr)
print(reverse_arr)