from player import Player
from  random import randint

class CPUPlayer(Player):
    def play(self):
        return randint(1, 3)