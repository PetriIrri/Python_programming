# Store what number the user number needs to be divisible with to get FIZZ or BUZZ
# Traditionally divisible with 3 is Fizz and 5 is Buzz
FIZZ = 3
BUZZ = 5

'''
This function is used to ask the user for his number.
Checks that the number is positive.
It does not receive any parameters.
returns the integer number
'''
def askUser():
    tryAgain = True
    while tryAgain:
        try:
            number = int(input("Give me a positive number!\n"))
            if number < 0 : raise ValueError
            return number
        except (ValueError, TypeError):
            print("Give me a valid number!")

'''
This function is used to check if the number is Fizz or Buzz.
receives the following parameters:
    - number: The number to be checked
    - fizz: What the number needs to be divisible with to produce Fizz
    - buzz: what the number needs to be divisible with to produce Buzz
Returns the outcome: "Fizz", "Buzz" or if number is Fizz and Buzz returns "FizzBuzz"
'''
def fizzBuzz(number, fizz, buzz):
    # Check if the number is FIZZ
    if Fizz(number, fizz):
        # check if it is also a BUZZ
        if Buzz(number, buzz):
            # The number is FizzBuzz!
            return "FizzBuzz"
        # The number is only Fizz
        else:
            return "Fizz"
    # Check if the number is Buzz
    elif Buzz(number, buzz):
        return "Buzz"
    # the number wasn't buzz or fizz. Return the number
    else:
        return str(number)

'''
This functions checks if the given number is fizz.
Receives following parameters:
    - number: the number to be checked
    - fizz: What the number needs to be divisible with to produce fizz
returns True or False based on whetever the number is fizz or not. 
'''
def Fizz(number, fizz):
    # check if the given number is divisible with fizz
    if number % fizz == 0: return True
    return False

'''
This functions checks if the given number is buzz.
Receives following parameters:
    - number: the number to be checked
    - buzz: What the number needs to be divisible with to produce buzz
returns True or False based on whetever the number is buzz or not. 
'''
def Buzz(number, buzz):
    # Check if the given number is buzz
    if number % buzz == 0: return True
    return False

def main():
    # Ask user for his number
    print("Hello and welcome to FIZZ BUZZ! I will tell you if a number is FIZZ or BUZZ.")
    number = askUser()
    # Print the outcome
    print(fizzBuzz(number, FIZZ, BUZZ))

if __name__ == "__main__":
    main()