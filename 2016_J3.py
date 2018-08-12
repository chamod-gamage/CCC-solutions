word = input()
palindrome = 0
if len(word)==1:
    palindrome = 1
for i in range(len(word)):
    for j in range(min(len(word[:i+1]),len(word[i:]))+1):
        if word[i-j:i+1] == word[i:i+j+1][::-1] and j*2 + 1 > palindrome:
            palindrome = j*2 + 1
        if i+j < len(word)-1:

            if word[i-j:i+1] == word[i+1:i+j+2][::-1] and  j*2 +2 > palindrome:
                palindrome = j*2 + 2

print(palindrome)



