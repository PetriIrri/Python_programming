from conversion import Conversion

class TemperatureConversion(Conversion):
    def __init__(self, value, source, destination):
        self.value = value
        self.source = source
        self.destination = destination

    def convert(self):
        return self.value * 1.8 + 32

    def convertBack(self):
        return (self.value - 32) / 1.8