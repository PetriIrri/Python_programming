# aks the user for a word and count the number of different letters
userInput = input("Give me a word and I will tell you how many different letters there are!")
lettersDict = {}
for letter in userInput:
    if letter in lettersDict:
        lettersDict[letter] = lettersDict[letter] + 1
    else:
        lettersDict[letter] = 1
print(lettersDict)