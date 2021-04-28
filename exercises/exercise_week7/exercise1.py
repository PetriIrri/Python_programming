import random

class Dice():
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class D6(Dice):
    def __init__(self,):
        super().__init__(6)

class D20(Dice):
    def __init__(self,):
        super().__init__(20)


def main():
    d6 = D6()
    print(d6.roll())
    d20 = D20()
    print(d20.roll())
    customDice = Dice(200)
    print(customDice.roll())


if __name__ == "__main__":
    main()