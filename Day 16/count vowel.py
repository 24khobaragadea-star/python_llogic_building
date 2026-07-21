def countvowels(word):
    count=0
    vowel="aeiou"

    for ch in word:
        if ch in vowel:
            count=count+1
    return count

    
print(countvowels("aarya khobaragade"))

