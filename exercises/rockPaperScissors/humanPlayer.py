from player import Player

class HumanPlayer(Player):
    def play(self):
        # Loop continues as long as player does not give valid input
        while True:
            # ask player for his choice and return the int value
            output = int(input("Give your choice!(1 = Rock, 2 = Paper, 3 = scissors)\n"))
            if output <= 4 and output > 0:
                return output
            else:
                print("Please give a value between 1-3!")