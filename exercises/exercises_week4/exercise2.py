def biggest(*numbers):
    if numbers:
        result = numbers[0]
        for number in numbers:
            if number > result:
                result = number
        return result
    else:
        return "No numbers given"

def smallest(*numbers):
    if numbers:
        result = numbers[0]
        for number in numbers:
            if number < result:
                result = number
        return result
    else:
        return "No numbers given"

print("Biggest number is:",biggest(1,2,3,4))
print("Smallest number is:", smallest(1,2,-3,4))