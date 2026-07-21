def palindrome(word):
    palindrome=True

    for index in range(len(word)) :
        if word[index]!=word[len(word)-1-index]:
            palindrome=False
        

    return palindrome

print(palindrome("mada"))