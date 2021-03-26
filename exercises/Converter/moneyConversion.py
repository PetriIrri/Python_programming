from conversion import Conversion

class MoneyConversion(Conversion):
    def __init__(self, value):
        # create objects for different conversions
        self.poundAndEur = self.PoundAndEur(value)
        self.eurAndUsd = self.EurAndUsd(value)
        self.poundAndUsd = self.PoundAndUsd(value)

    # Makes conversions between € and £
    class PoundAndEur:
        def __init__(self, value):
            self.value = value
            self.source = "€"
            self.destination = "£"

        # Converts € to £
        def convert(self):
            return self.value * 0.85572111

        # converts £ to €
        def convertBack(self):
            return self.value * 1.1685484

    # Makes conversions between € and $
    class EurAndUsd:
        def __init__(self, value):
            self.value = value
            self.source = "€"
            self.destination = "$"
        
        # converts € to $
        def convert(self):
            return self.value * 1.1779056

        # converts $ to €
        def convertBack(self):
            return self.value * 0.84896448

    # Makes conversions between £ and $
    class PoundAndUsd:
        def __init__(self, value):
            self.value = value
            self.source = "£"
            self.destination = "$"
        
        # converts £ to $
        def convert(self):
            return self.value * 1.3766828

        # converts $ to £
        def convertBack(self):
            return self.value * 0.72638376