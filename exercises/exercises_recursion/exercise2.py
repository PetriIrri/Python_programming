def numbers(number: int):
    if number < 0:
        return "only positive numbers please!"
    elif number < 10:
        return 1
    else:
        return 1 + numbers(number / 10)

userInput = int(input("Give me a number! \n"))
print("there are:", numbers(userInput), "numbers!")