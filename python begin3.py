getal1 = 3
getal2 = 8
getal3 = getal1 + getal2
print (getal3)
stad = input("wat vind jij een leuke stad")
if stad == "Amsterdam":
    print ("dat is mijn favoriete stad")
getal = input("ik heb een cijfer in mijn hoofd kan jij het raden wat is het getal. ")
if getal == "4":
    print("je hebt 4 precies geraden")
elif getal == "6":
    print("Zes is een perfect getal")
warmte = int(input("Hoe warm is het "))
if warmte < 20:
    print("brr koud")
else:
    print("Lekker warm")
oud = int(input("Hoe oud ben jij "))
if oud < 18:
    print("Haahahahahahahahahah je bent nog niet volwassen")
else:
    print("Gefelicieerd je bent volwassen")
print("bedankt voor je deelname")
nummer = int(input("raad een nummer onder de 10 "))
if nummer == "9":
    koekje = input("Je hebt gewonnen! Wil je een koekje? ")
    if koekje == "ja":
        print("Alsjeblieft!")
    else:
        print("Ok, dan geen koekje.")
else:
    print("Helaas dat klopt niet!")
code = input ("Probeer de geheime code te raden: ")
if code == "+":
    code2 = input("")
    if code2 == "a":
        print("Je hebt het gevonden!")
    else:
        print("Helaas dat klopt niet!")
else:
    print("Helaas dat klopt niet!")
print("Doei!   ")
woord = input("Noem een woord van 5 letters ")
if len(woord) == 5:
    print("goed gedaan")
else:
    print("sorry dat is fout")