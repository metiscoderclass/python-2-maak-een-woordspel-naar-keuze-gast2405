import random

randomizer1 = random.randrange (1,3,1)
randomizer2 = random.randrange (1,3,1)
randomizer3 = random.randrange (1,3,1)
randomizer4 = random.randrange (1,3,1)

naam = input("hoe wil je jezelf noemen ")
if naam == "Monstro":
    print("Het is weer een saaie dag zoals altijd helemaal alleen gevangen in een kleine kamer, .... Bam!! de deur die opgesloten zat vliegt opeens open er komt een kleine man uit je wilt graag vrienden met hem zijn je springt met blijheid in de lucht alleen toen je landde rende die man weg en hij Schoot op je!! Nu is het genoeg Je rent naar hem toe om hem kijhard te slaan. Het mens s doodt er komt shuim uit zijn mond hij ziet er niet goed uit. Voor je het weet wordt het zwart en wanneer je je ogen weer open kan doen zie je jezelf je schrikt je wilt opstaan om te zien wat er aan de hand is alleen het lukt niet je kan niet bewegen er komt schuim uit je mond. je hoort zachtjes ")
    back = True
    while back == True:
        print("error")
else:
    intro = input("Hallo " + naam + ", jij bent gevallen in een grot een oneindige grot nog wel. Je ziet voor je een donker pad maar je wilt liever hier blijven. Wat ga je doen, weggaan of hier blijven ")
    if intro == "weggaan":
        verdergaan = input ("Je hebt besloten om weg te gaan. het is een eind lopen maar uiteindelijk zie je wat licht met hoop ren je er naar toe. je kijkt om je heen het is een lege kamer met een kist je wit gaan kijken of er iets handigs in de kist zit maar dan bedenk je dat het ook een val kan zijn terwijl je zi te nadenken valt er een gigantische spin van het dak. wat ga je doen, wegrennen, rennen naar de kist, val de spin aan met blote handen ")
        if verdergaan == "wegrennen":
            print("je rent terug naar het begin alleen maar om te sterfen van de honger !je bent dood!")
        elif verdergaan == "rennen naar de kist":
            verder = input("je vindt een shotgun in d kist je vermoord de spin wat ga je nu doen, jezelf vermoorden, ga terug naar huis , ga verder ")
            if verder == "ga verder":
                verder2 = input("je gaat naar de volgende kamer daar blijken zombies te zitten gelukkig kan je hun met je shotgun vermoorden een van die zombies heeft een sluitel laten vallen je houdt het bij je het is nogal makkelijk alle kamers met je shotgun tot je bij een gouden kamer komt er zit een klein dingetje op wat zit er op. verdorven melk, je drinkt het/eet het omdat je moet wat eten. om eerijk te zijn smaakte het geweldig je hoorde een klein stemmetje in je hoofd dat zegt 'extra leven' je gaat naar de volgende kamer er ligt een sleutel in en een deur die op slot zit. open de deur of ga verder ")
                if verder2 == "open de deur":
                    print("het is een shop je hebt maar 3 euro er is niks in de shop voor maar 3 euro dus je gaat verder er zit een klein wezentje in gellukig heb je nog die shotgun, die gast had 2 euro maar nu niet meer je kijkt om je heen en oh oh je zit een deur met het tekentje van een monster erop het is de enige deur dus je moet naar binnen ga terug naar de shop of vecht de baas PS:ga naar python 5 en typ in '3468' ")
                elif verder2 == "ga verder":
                    print("je gaat verder er zit een klein wezentje in gellukig heb je nog die shotgun, die gast had 2 euro maar nu niet meer je kijkt om je heen en oh oh je zit een deur met het tekentje van een monster erop het is de enige deur dus je moet naar binnen ga terug naar de shop of vecht de baas PS:ga naar python 5 en typ in '2841'")
            elif verder == "jezelf vermoorden":
                print (naam + " is doodt")
            elif verder == "ga terug naar huis":
                print ("je gaat terug naar huis je neemt het vlees van de spin mee wanneer je thuis bent eet je wat vlees het bleek vergifteging te zijn !!Je bent doodt!! ")
            else:
                print ("zo kan je niet antwoorden !!Je bent doodt!!")
        elif verdergaan == "val de spin aan met blote handen":
            print("je valt de spin aan maar met zijn klauwen vermoord het je !je bent dood!")
        else:
            print("je wordt aangevallen !je bent dood!")
    elif intro == "hier blijven":
        print("je hebt besloten om te blijven. na 5 dagen begin je toch honger te krijgen je besluit toch om we te gaan want als je niks doet ga je doodt.")
        verdergaan = input ("het is een eind lopen maar uiteindelijk zie je wat licht met hoop ren je er naar toe. je kijkt om je heen het is een lege kamer met een kist je wit gaan kijken of er iets handigs in de kist zit maar dan bedenk je dat het ook een val kan zijn terwijl je zi te nadenken valt er een gigantische spin van het dak. wat ga je doen, wegrennen, rennen naar de kist, val de spin aan met blote handen ")
        if verdergaan == "wegrennen":
            print("je rent terug naar het begin alleen maar om te sterfen van de honger !je bent dood!")
        elif verdergaan == "val de spin aan met blote handen":
            print("je valt de spin aan maar met zijn klauwen vermoord het je !je bent dood!")
        elif verdergaan == "rennen naar de kist":
            verder = input("je vindt een shotgun in d kist je vermoord de spin wat ga je nu doen, jezelf vermoorden, ga verder , eet het vlees ")
            if verder == "eet het vlees":
                print("het vlees bleek vergiftigd te zijn. !je bent dood!")
            elif verder == "jezelf vermoorden":
                print (naam + " is doodt")
            elif verder == "ga verder":
                print ("je wilt verder gaan alleen voor je de deur open doet val je van de honger je schreeuwt van de pjin!")
                honge = input("je krijgt pijn in je buik je ziet nog steeds wat vlees op de grond liggen maar in de volgende kamer ligt ook eten of is dat te veel moeite misschien als je niks doet gaat het over wat ga je nu doen! ga verder, ga terug naar het vlees, blijf liggen ")
                if honge == "ga verder":
                    print("in de volgende kamer zitten zombies je had je shotgun laten vallen dus je kan niks doen. !je bent dood!")
                elif honge == "ga terug naar het vlees":
                    print ("je was net dichtbij genoeg om het te pakken alleen het was niet te smaken er zat gif in! !je bent dood!")
                elif honge == "blijf liggen":
                    print("De pijn het wordt sterker het lijkt alsof er een beest uit je buik komt of is dat een hallucinatie? er komt een zwart opgerold wezen uit je buik de pijn is onverdraagelijk maar voor je doodt gaat zegt het wezen iets: 'pap ik ben het kinka' !je bent doodt?!")
                    print("Secret als je aan het begin kinka invoert krijg je een secret")
    elif intro == "kinka":
        secret = input("Je hebt een secret gevonden, je hebt nu een kleine baby naast je de kleine baby groeit en groeit en groeit. De baby zegt dat hij je niet meer aan kan kijken hij slaat je. het voelt alsof 20 jaar opeens voorbij is. jullie beginnen te vechten, wat a je doen? ren weg, ren naar de baby, ontwijk zijn aanvallen of probeer het uit te praten ")
        if secret == "ren weg":
            print("je rent weg alleen een gigantishe spin valt op je hoofd je bent te gestrest je hebt geen idee wat er gebeurt !!Je bent doodt!!")
        elif secret == "ren naar de baby":
            print("de baby slaat je in de lucht je vliegt omhoog voor uren teminste zo voelde het uiteindelijk landt je op gras. Jij bent uit de grot. met grote frustratie loop je naar een bos, je bent bang en dan wordt het opeens zwart je wordt wakker in de grot. je hoort zachtjes weltrusten")
        elif secret == "ontwijk zijn aanvallen":
            print("je probeert zijn aanvallen te ontwijken het lukt niet !!Je bent doodt!!")
        elif secret == "probeer het uit te praten":
            print("het lukt niet !!Je bent doodt!!")
        else:
            print("Je hebt verkeerd geantwoord !!Je bent doodt!!")
    else:
        print("sorry zo kan je niet antwoorden. !je bent dood!")