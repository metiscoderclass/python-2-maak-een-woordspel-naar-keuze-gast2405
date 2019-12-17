a = 4
b = 5
c = 6
d = "hallo"
print(1, a > b)
print(2, 4 != 4)
print(3, 4 == (7 - 3))
print(4, b - a == a)
print(5, "hallo" == "hallo")
kopen = input("Hallo, wilt u appels of peren? ")
if kopen == "peren":
    aantal = input("Hoeveel peren wilt u? ")
    print("Oke! Wij sturen u " + aantal + " peren!")
elif kopen == "appels":
    aantal = input("Hoeveel appels wilt u? ")
    print("Oke! Wij sturen u " + aantal + " appels!")
else:
    print("dat mag niet")
warmte = int(input("Hoe warm is het "))
if warmte > 15:
    print("je kan zonder jas naar buiten")
elif warmte < 0:
    print("Het vriest!")
elif warmte < 16:
    print("Trek een jas aan als je naar buiten gaat!")
jaar = input("welk jaar is het")
geboortejaar = input ("in welk jaar ben jij geboren")
leeftijd = input("hoe oud ben jij")
rekenen = geboortejaar + leeftijd
if rekenen == jaar:
    print("Je bent dit jaar al jarig geweest.")
elif rekenen < jaar:
    print("Je bent dit jaar niet jarig geweest.")
getal = 6
anderegetal = input("noem een getal")

if getal == anderegetal:
    print("Het getal is hetzelfde")
else:
    print("Het getal is niet hetzelfde")