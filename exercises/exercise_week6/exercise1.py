def leapYear(year):
    # Check if year is a leap year
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# ask the user what year he would like to check
print("I will tell you if a year is a leap year!")
year = int(input("Tell me the year!\n"))
# check the answer
print("The answer is:", leapYear(year))