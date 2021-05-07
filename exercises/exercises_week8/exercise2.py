def getPrimeNumbers(num):
    output = ""
    if num < 2:
        pass
    else:
        # check every number from 2 to num.
        for number in range(2, num + 1):
            # check if the current number is divisible
            for i in range(2, number):
                if(number % i) == 0:
                    # number was divisible with i Break loop.
                    break
            else:
                # loop completed succesfully. Number is only divisible with itself and 1
                output += str(number) + "\n"
        return f"The prime numbers are \n{output}"

def main():
    print(getPrimeNumbers(100))

if __name__ == "__main__":
    main()