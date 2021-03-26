class Conversion:
  def __init__(self, value):
    self.value = value
    self.source = ""  # Lähdeyksikkö, esim. €
    self.destination = ""  # Kohdeyksikkö, esim. $

  def convert(self):
    ''' Tekee yksikkömuunnoksen lähdeyksiköstä kohdeyksikköön '''
    return 1

  def convertBack(self):
    ''' Tekee yksikkömuunnoksen kohdeyksiköstä lähdeyksikköön '''
    return 1