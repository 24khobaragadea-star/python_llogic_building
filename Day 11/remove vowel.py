word="aarya khobaragade"
vowels = "aeiou"
removed=""

for ch in word:
    if ch not in vowels:
        removed=removed+ch
print(removed)