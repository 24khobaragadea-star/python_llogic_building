word="aarya khobaragade "
seen=""

for ch in word:
    if ch not in seen:
        seen=seen+ch
    else:
        print("duplicate: ",ch)
print(seen)
