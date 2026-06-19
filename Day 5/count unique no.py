arr=[1,2,3,4,4,3,5,6,7,2,3,7]

seen=[]
for num in arr:
    if num not in seen :
    
        seen.append(num)
print(seen)
print(len(seen))
