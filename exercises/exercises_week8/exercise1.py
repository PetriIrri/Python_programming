# Harjoitus 1:
#
# Kirjoita funktio, joka korottaa numeron x potenssiin n.
# Funktio ottaa vastaan kaksi parametria, kantaluvun x
# ja exponentin n. Älä käytä operaattoria ** tai
# funktiota pow. Ota huomioon myös negatiiviset exponentit.
#
# a) Kirjoita funktiosta silmukkaan perustuva versio.
# b) Kirjoita funktiosta rekursiivinen versio.

def solutionA(x, n):
    if n < 0:
        negative = True
        n = abs(n)
    else:
        negative = False
    # first check if n is 0
    if n == 0:
        # exponent is 0 return 1
        return 1
    output = x
    for i in range(1, n):
        output *= x
    if negative:
        return f"1 / {output}"
    else:
        return output

def solutionB(x, n):
    # first check if n is 0
    if n == 0:
        # exponent is 0 return 1
        return 1
    elif n < 0:
        negative = True
        n = abs(n)
    else:
        negative = False

    if negative:
        return f"1 / {x * solutionB(x, n - 1)}"
    else:
        return x * solutionB(x, n - 1)

def main():
    print(solutionA(3, 3))
    print(solutionB(3, -3))

if __name__ == "__main__":
    main()
