# LISTS ARE THE MOST IMP TOPIC FOR DSA , A LIST CAN STORE MULTIPLE VALUES IN ONE VARIABLE , WE CAN STORE
# DIFFERENT DATA TYPES TOO IN SAME LIST , THEY ARE MUTABLE I.E WE CAN CHANGE THEIR VALUES . 

numbers = [10, 20, 10, 30, 40, 20, 50]
list=[]

for num in numbers:
    if num not in list:
        list.append(num)
print(list)