myList = ["one", "two", "three", "four", "five"]
# create a new list to which we put the numbers in reverse order
reversedList = []
# start at the last index of myList and append to reversedList.
# Then - 1 from index and loop again until all values are in reversedList
index = len(myList) - 1
while index >= 0:
    reversedList.append(myList[index])
    index -= 1

for number in reversedList:
    print(number)