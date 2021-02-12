def isPalindrome(string: str = "saippua\t kivi\n kauppias"):
    string = "".join(string.split()).lower()
    reversed = string[::-1]
    if string == reversed:
        return "String is a palindrome!"
    else:
        return "String is not a palindrome!"

print(isPalindrome())