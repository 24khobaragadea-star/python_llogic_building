word= "  aarya   khobaragade  "
count=0

for index in range(len(word)):

    if (index==0 and word[index]!=" ")  or (word[index]!=" " and word[index-1]==" "):
        count=count+1
print(count)

