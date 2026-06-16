arr=[1,2,3,4,5,6]
index=5
reverse_arr= []

for num in arr:
    reverse_arr.append(arr[index])
    index=index-1
print(reverse_arr)