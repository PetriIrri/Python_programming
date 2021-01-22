# Muuttujien määrittäminen. Python tulkki osaa päätellä muuttujan tyypin sen arvosta.
var1 = 1 #Integer
var2 = "text" # String

print(var1)

# Python on dynaamisesti tyypitetty kieli
# Muuttujan tyyppi päätellään ajon aikana, kun muuttujan alustava rivi suoritetaan
# Muuttujan tyypin pystyy muuttamaan määrittämällä muuttuja uudelleen

var1 = "text1" # Muuttujan tyyppi muuttui integeristä stringisksi

print(var1)

var3 = 1.2 # Float, desimaaliluku
var4 = True # Boolean, totuusarvo (True tai False)

numero1 = 2
numero2 = 4

tulos = 0

# Yhteenlasku
tulos = numero1 + numero2

print(tulos)

# tulos = tulos - numero1
tulos -= numero1

print(tulos)


#jakolasku
# Tulos Float-tyyppiä vaikka molemmat jaettavat ovat kokonaislukuja
tulos = numero1 / numero2

#jakolasku joka palauttaa kokonaisluvun
tulos = numero1 // numero2

#python on vahvasti tyypitetty kieli
muuttuja1 = 10
muuttuja2 = "tekstiä"

# Esimerkiksi eri tyyppisten muutujien yhteenlasku ei ole mahdollista
# print(muuttuja2 + muuttuja1)

# Koodaajan vastuulla on suorittaa tyyppimuunnos
# Esim. ala oleva koodi muuttaa kokonaisluvun merkkijonoksi, jonka jälkeen lisäys toimii
print(muuttuja2 + str(muuttuja1))

# Lainausmerkit
print("Tulostuu!")

print('Tulostuu tämäkin!')

print('Tämä on "lainaus"')
print("Tämä on myös \"lainaus\"")
# Lainausmerkit voidaan merkitä kenoviivalla, jolloin ne tulkitaan osaksi merkkijonoa
# print("Tämä ei toimi') Tällä tavpom lainausmerkkejä ei voi yhdistää

# Rivinvaihto pitkillä teksteillä hoituu kenoviivalla, mikäli haluamme rivittää sen useammalle riville
print("Rivinvaihtoa \
Jee")
# Kolmella lainausmerkillä onnistuu myös
longText = """Lorem ipsum
dolor sit amet"""

print(longText)

# Usean rivin kommenttina pythonissa voidaan käyttää """ operaattoria
""" Tämä
on usean rivin 
kommentti
"""

print("Yllä oleva toimii kommenttina")

# Tyyppimuunnoksia
# int(muuttuja) muuttaa muuttujan integeriksi
# float(muuttuja) muuttaa muuttujan desimaaliluvuksi
# str(muuttuja) muuttaa muuttujan stringiksi

# boolean eli totuusarvo
# arvo 0 vastaa totuusarvoa False, mikä tahansa muu vastaa totuusarvoa true
print(bool(0))