def romanToNum(value = str):
    dictio = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    number = 0
    i = 0
    while i < len(value):
        # check if the next two characters form a roman number and exist in dictionary
        if i != len(value) - 1 and value[i] + value[i + 1] in dictio:
            number += dictio[value[i] + value[i + 1]]
            i += 2
        else:
            number += dictio[value[i]]
            i += 1
    return number


def numToRoman(value = int):
    dictio = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'x', 9: 'IX', 5: 'V', 4:'IV', 1:'I'}
    # Variable that stores the roman numerals answer
    roman = ""
    while value > 0:
        for number in dictio.keys():
            if number <= value:
                value -= number
                roman += dictio[number]
                break
    return roman

def main():
    print("Numero roomalaisittain:", numToRoman(2000))
    print("Roomalainen käännettynä:", romanToNum("MM"))

if __name__ == "__main__":
    main()