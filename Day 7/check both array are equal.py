arr1=[1,2,3,4,5]
arr2=[1,2,3,4,5]
equal=True


for index in range(len(arr1)):
    if arr1[index]!=arr2[index]:
        
        equal=False
        break

if equal:
    print("array equal")
else:
    print("array not equal")
