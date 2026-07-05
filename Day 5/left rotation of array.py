arr=[1,2,3,4,1,23,4]
first=arr[0]



## another main approach without remove and append 

for index in range(len(arr)-1):

        
        arr[index]=arr[index+1]
arr[len(arr)-1]=first       
print(arr)

    