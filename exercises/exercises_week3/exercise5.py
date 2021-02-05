# ask the user from how many numbers he wants an average then ask the numbers and count average
count = int(input("From how many numbers do you want to  calculate the average?"))
sum = 0
i = 0
# ask the user for the numbers
while i < count:
    sum += int(input("Give me a number!"))
    i += 1
# Just wanted the average as an integer. IT IS NOT accurate, integers are rounded down.
print("Average of all the given numbers is: " + str(int(sum / count)))
