from temperatureConversion import TemperatureConversion
from moneyConversion import MoneyConversion

def tempConversion():
    # ask user how he would like to convert
    print("How would you like to convert? 1 = Celcius -> fahrenheit, 2 = Fahrenheit -> Celcius")
    success = False
    while not success:
        choice = readInput()
        if choice == 1:
            # create TemperatureConversion object and pass to it the temperature and source and destination
            print("Give me the temperature!")
            temp = TemperatureConversion(readInput(), "°C", "°F")
            # call the objects convert function
            converted = temp.convert()
            # print the result
            print(temp.value, temp.source, "-->", converted, temp.destination)
            success = True
        elif choice == 2:
            # create TemperatureConversion object and pass to it the temperature and source and destination
            print("Give me the temperature!")
            temp = TemperatureConversion(readInput(), "°F", "°C")
            # since we are converting to celsius call convertBack function
            converted = temp.convertBack()
            # print result
            print(temp.value, temp.source, "-->", converted, temp.destination)
            success = True
        else:
            print("not a valid choice! Give me a new value!")

def monConversion():
    # Ask user about what kind of conversions he wants
    print("What kind of conversion do you want to do? 1 = EUR and GBP, 2 = EUR and USD, 3 = GBP and USD")
    success = False
    while not success:
        choice = readInput()
        # If choise is valid: create a moneyConversion object that has inner classes for other possible conversions
        if choice == 1:
            # ask user for the value
            print("Give me a value")
            money = MoneyConversion(readInput())
            # do the conversions. Could perhaps have made this easier to read...
            print(money.poundAndEur.value, money.poundAndEur.source, "-->", money.poundAndEur.convert(), money.poundAndEur.destination)
            print(money.poundAndEur.value, money.poundAndEur.destination, "-->", money.poundAndEur.convertBack(), money.poundAndEur.source)
            success = True
        elif choice == 2:
            print("Give me a value")
            money = MoneyConversion(readInput())
            print(money.eurAndUsd.value, money.eurAndUsd.source, "-->", money.eurAndUsd.convert(), money.eurAndUsd.destination)
            print(money.eurAndUsd.value, money.eurAndUsd.destination, "-->", money.eurAndUsd.convertBack(), money.eurAndUsd.source)
            success = True
        elif choice == 3:
            print("Give me a value")
            money = MoneyConversion(readInput())
            print(money.poundAndUsd.value, money.poundAndUsd.source, "-->", money.poundAndUsd.convert(), money.poundAndUsd.destination)
            print(money.poundAndUsd.value, money.poundAndUsd.destination, "-->", money.poundAndUsd.convertBack(), money.poundAndUsd.source)
            success = True
        else:
            print("not a valid choice! Give me a new value!")

def readInput():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Not an integer!")

def main():
    # ask user in what mode he would like to use this program
    print("Hello what would you like to do? 1 = temperature converter and 2 = money converter")
    success = False
    while not success:
        choice = readInput()
        if choice == 1:
            success = True
            tempConversion()
        elif choice == 2:
            success = True
            monConversion()
        else:
            print("Not a valid choice! Give a new value!")

if __name__ == "__main__":
  main()