def multiplicator(*numbers):
    # Loop through the given numbers
    for iteration, number in enumerate(numbers):
        # on first iteration initialize result with the first given number
        if iteration == 0:
            result = number
        else:
            # on successive iteration multiply
            result = result * number
    return result

print(multiplicator(1,2,3,4))
