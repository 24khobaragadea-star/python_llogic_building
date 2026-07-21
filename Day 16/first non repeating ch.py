def repeat(word):
    for ch in word:
        if word.count(ch)==1:
            return ch
        
print(repeat("aarya"))