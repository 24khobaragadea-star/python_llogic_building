word = "AI@DS#2026!"
count=0

for ch in word:
    if not ('a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9'):
        count=count+1
print(count)


      