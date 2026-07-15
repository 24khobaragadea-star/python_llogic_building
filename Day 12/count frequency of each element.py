word="aarya"
seen=""


for ch in word:
    if ch not in seen:
        seen=seen+ch
        count=0
        
        for x in word:
          if x==ch:
            count=count+1
        
        

        
        print(ch,":" ,count)

        