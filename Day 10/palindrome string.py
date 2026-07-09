word="madama"
palindrome=True

for index in range(len(word)):
    if word[index]!=word[len(word)-1-index]:
        palindrome=False
        break

if palindrome:
    print("string is palindrome ")
else:
    print("string is not palindrome")