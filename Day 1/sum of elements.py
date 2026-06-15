arr=[4,7,2,9,1]

total=arr[0]+arr[1]
total1=total+arr[2]
total2=total1+arr[3]
total3=total2+arr[4]
print(total3)

## efficient code 
totaln=0
for num in arr:
    totaln=totaln+num
print(totaln)