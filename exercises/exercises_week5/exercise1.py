import random

def numberGuessing(i = int):
    tryAgain = True
    while tryAgain:
        try:
            # ask user for his number
            userInput = int(input("What do you think the number could be?\n"))
            # check if the number is correct
            if userInput == i:
                print("You guessed it right!")
                tryAgain = False
            elif userInput > i:
                print("The number is smaller than that!")
            elif userInput < i:
                print("The number is bigger than that!")
        except TypeError:
            print("Give me a valid value!")
        except ValueError:
            print("Give me a valid value!")

# get a random integer
randInt = random.randint(1, 9)
print("Welcome to our nightshow! Today we are guessing random numbers! Do you have what it takes?")
print("the number is between 1-9")
numberGuessing(randInt)