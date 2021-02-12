def numOfVocals(string: str = "SaIppuAkivIkaUppiAs"):
    # A dictionary for the vocals.
    vocals = {"a", "e", "i", "o", "u", "y", "ä", "ö"}
    result = 0
    # Transform the string to lowercase and start counting vocals
    for letter in string.lower():
        if letter in vocals:
            result += 1
    return result

print(numOfVocals(), "vocals!")