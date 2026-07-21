def count(word):
    vowel=0
    consonent=0
    vowel1='aeiou'

    for ch in word:
        if ch in vowel1:
            vowel=vowel+1

        else:
            consonent=consonent+1
    
    return vowel,consonent
           
print(count("aarya khobaragade"))