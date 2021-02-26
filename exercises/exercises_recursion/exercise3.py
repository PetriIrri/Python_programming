def isPalindrome(word, first, last):
    if first == last or first > last:
        return True
    elif word[first] == word[last]:
        return isPalindrome(word, first + 1, last - 1)
    else:
        return False

word = input("Give me a word and I will check if it is a palindrome\n")
word = word.lower()
# Delete all white spaces
word = "".join(word.split())

if isPalindrome(word, 0, len(word) - 1):
    print("Word is a palindrome :)")
else:
    print("Word is not a palindrome :(")