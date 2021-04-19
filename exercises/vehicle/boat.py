from vehicle import Vehicle
from values import Terrain

class Boat(Vehicle):
    def __init__(self, x, y):
        super().__init__(1, x, y)
        self.name = "Vene"
        self.symbol = "V"
        

    def InitAllowedTerrains(self):
        ''' Määrittää millaisessa maastossa ajoneuvolla voi ajaa. Arvot values.Terrain-enumin arvoja.'''
        self.allowedTerrains = [Terrain.WATER]

    def GetName(self):
        ''' Palauttaa ajoneuvon nimen. '''
        return self.name

    def GetSymbol(self):
        ''' Palauttaa symbolin, jolla ajoneuvo piirretään karttaan. '''
        return self.symbol


def main():
    # test that we can create a car object
    boat = Boat(0, 0)
    print(boat.GetName())
    print(boat.GetSymbol())
    print(boat.allowedTerrains)
    print(boat.speed)
    print(boat.position)

if __name__ == "__main__":
    main()