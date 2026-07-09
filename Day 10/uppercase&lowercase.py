word="AAryA"
count_lower=0
count_upper=0
for ch in word:
    if ch.islower():
        count_lower=count_lower+1

    else:
        count_upper=count_upper+1

print(count_upper)
print(count_lower)


