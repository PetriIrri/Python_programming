# ask user for words as long as he does not write "stop". afterwards print them all out
print("Please give me a word!")
userInput = input()
# I want to store the words in a list. You could also create a big string to store them in.
wordList = []
while userInput != "stop":
    wordList.append(userInput)
    print("please give me MORE WORDS!")
    userInput = input()
# Print all the stored words
print("\nPrinting ALL the words!")
for x in wordList:
    print(x)