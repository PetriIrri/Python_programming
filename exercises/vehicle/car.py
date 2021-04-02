from vehicle import Vehicle
from values import Terrain

class Car(Vehicle):
    def __init__(self, x, y):
        self.name = "Auto"
        self.symbol = "A"
        self.speed = 2
        self.position = (x, y)
        self.InitAllowedTerrains()

    def InitAllowedTerrains(self):
        ''' Määrittää millaisessa maastossa ajoneuvolla voi ajaa. Arvot values.Terrain-enumin arvoja.'''
        self.allowedTerrains = [Terrain.GROUND]

    def GetName(self):
        ''' Palauttaa ajoneuvon nimen. '''
        return self.name

    def GetSymbol(self):
        ''' Palauttaa symbolin, jolla ajoneuvo piirretään karttaan. '''
        return self.symbol


def main():
    # test that we can create a car object
    car = Car(0, 0)
    print(car.GetName())
    print(car.GetSymbol())
    print(car.allowedTerrains)
    print(car.speed)
    print(car.position)

if __name__ == "__main__":
    main()