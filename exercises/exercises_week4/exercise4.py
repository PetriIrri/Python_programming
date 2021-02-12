def factorial(number: int = 0):
    # check if number is 0 or smaller.
    if number == 0:
        return 1
    elif number < 0:
        return "Number was negative!"
    else:
        multiplier = number
        result = 0
        # reduce multiplier by 1 for each iteration
        while multiplier > 1:
            multiplier -= 1
            result = number * multiplier + result
    return result

print("Factorial is:", factorial(4))
