names = [
    "Aarya",
    "Rahul",
    "Aarya",
    "Rahul",
    "Aarya",
    "Rahul",
    "Rahul"
]

frequency={}
for name in names:

    if name not in frequency:
      frequency[name]=1
    else:
      frequency[name]=frequency[name]+1

print(frequency)