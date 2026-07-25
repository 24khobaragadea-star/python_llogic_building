numbers = [10, 20, 30, 10, 20, 10, 40]
freq={}

for num in numbers:
    if num not in freq:
        freq[num]=1
    else:
        freq[num]=freq[num]+1

print(freq)