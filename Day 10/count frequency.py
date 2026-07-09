word="aarya"
seen=""
count=0

for ch in word:
    if ch not in seen:
        print("not in seen")
    else:
        count=count+1
        seen=seen+ch

print(count)


        
