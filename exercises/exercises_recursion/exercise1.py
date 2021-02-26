def fibonacci(n: int = 0):
    # if the number is 0 or 1 do nothing and return the number
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

input = int (input("Give me a number! \n"))
print("The fibonacci sequence is:")
for i in range(input):
    print(fibonacci(i))