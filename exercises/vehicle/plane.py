from vehicle import Vehicle
from values import Terrain

class Plane(Vehicle):
    def __init__(self, x, y):
        self.name = "Lentokone"
        self.symbol = "L"
        self.speed = 3
        self.position = (x, y)
        self.InitAllowedTerrains()

    def InitAllowedTerrains(self):
        ''' Määrittää millaisessa maastossa ajoneuvolla voi ajaa. Arvot values.Terrain-enumin arvoja.'''
        self.allowedTerrains = [Terrain.WATER, Terrain.GROUND]

    def GetName(self):
        ''' Palauttaa ajoneuvon nimen. '''
        return self.name

    def GetSymbol(self):
        ''' Palauttaa symbolin, jolla ajoneuvo piirretään karttaan. '''
        return self.symbol

def main():
    # test that we can create a car object
    plane = Plane(0, 0)
    print(plane.GetName())
    print(plane.GetSymbol())
    print(plane.allowedTerrains)
    print(plane.speed)
    print(plane.position)

if __name__ == "__main__":
    main()