list1 = [10, 20, 30, 40, 50, 60]
list2 = [20, 40, 60, 80, 100]

result=set(list1)| set(list2)
print(result)
result1=set(list1)-set(list2)
result2=set(list2)-set(list1)
print(result1)
print(result2)