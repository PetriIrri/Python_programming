# Count how many even and odd numbers there are in a given list.
numbers = (3, 1, 6, 3, 4, 7, 0, 6, 3, 2, 6, 8, 3)
odd = 0
even = 0
for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print("there were " + str(even) + " even numbers")
print("there were " + str(odd) + " odd numbers")
