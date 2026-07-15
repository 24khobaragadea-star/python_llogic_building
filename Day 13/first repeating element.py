word="Abc"
seen=""

for ch in word:
    if ch not in seen :
        seen=seen+ch
    else:
        print(ch)
        break





















