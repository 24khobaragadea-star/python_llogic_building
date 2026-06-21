arr=[1,2,3,2,1]
palindrome=True

for index in range(len(arr)//2):
    if arr[index]!=arr[len(arr)-1-index]:
        palindrome=False
        
if palindrome:
    print("array is palindrome")   
else:
    print("array is not palindrome")
        