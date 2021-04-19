def checkDuplicates(testList):
    # transform the list to a set
    testSet = set(testList)
    # sets can have only unique values so if the lenghts differ; there were duplicates
    if len(testList) == len(testSet):
        return False
    else:
        return True

testList = [1,4,"hello",3,2,6,"Hello","Hello", 1]
# Check if there are duplicates in the list
duplicates = checkDuplicates(testList)
# Print the answer!
print("does the list contain duplicates o great machine! -->", duplicates)