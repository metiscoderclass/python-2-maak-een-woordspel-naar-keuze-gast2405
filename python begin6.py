slecht = "niks"
goed = "niks"
array = ["0","1","2","3","4","5","6","7","8","9","10"]
back = True
while back == True:
    dag = input("Hallo, hoe was je dag vandaag ")
    back = False
    if dag == "slecht":
        slecht = input("oh dat is niet goed waarom? ")
    elif dag == "goed":
        goed = input("Dat is fijn om te horen waarom ben je zo blij ")
    else:
        print("sorry ik ben alleen geprogammeerd om te antwoorden op GOED en SLECHT")
        back = True
        
back2 = True
while back2 == True:
    back2 = False
    rate = input("als je je dag een cijfer onder de 10 zou geven wat is dat dan? ")
    if rate == array[0]:
        if slecht == "niks":
            print("oh maar net zei je: " + goed + " dus dat meende je niet echt?")
        elif goed == "niks":
            print("niet je lievelings dag hè")
    elif rate == array[1]:
        if slecht == "niks":
            print("oh maar net zei je dat je blij was " + goed + " dus dat meende je niet echt?")
        elif goed == "niks":
            print("niet je lievelings dag hè")
    elif rate == array[2]:
        if slecht == "niks":
            print("oh maar net zei je dat je blij was " + goed + " dus dat meende je niet echt?")
        elif goed == "niks":
            print("niet je lievelings dag hè")
        
    elif rate == array[3]:
        if slecht == "niks":
            print("oh maar net zei je dat je blij was " + goed + " dus dat meende je niet echt?")
        elif goed == "niks":
            print("niet je lievelings dag hè")
        
    elif rate == array[4]:
        if slecht == "niks":
            print("oh maar net zei je dat je blij was " + goed + " dus dat meende je niet echt?")
        elif goed == "niks":
            print("niet je lievelings dag hè")
        
    elif rate == array[5]:
        if slecht == "niks":
            print("ok mischien niet de beste dag maar je bent gelukkig blij")
        elif goed == "niks":
            print("Het kan ook slechter")
        
    elif rate == array[6]:
        if slecht == "niks":
            print("ok mischien niet de beste dag maar je bent gelukkig blij")
        elif goed == "niks":
            print("Het kan ook slechter")
        
    elif rate == array[7]:
        if slecht == "niks":
            print("nou goed om te horen dat het zo geweldig ging")
        elif goed == "niks":
            print("oh dus dat " + slecht + "is dus niet zo erg")
    
    elif rate == array[8]:
        if slecht == "niks":
            print("nou goed om te horen dat het zo geweldig ging")
        elif goed == "niks":
            print("oh dus dat " + slecht + "is dus niet zo erg")
        
    elif rate == array[9]:
        if slecht == "niks":
            print("nou goed om te horen dat het zo geweldig ging")
        elif goed == "niks":
            print("oh dus dat " + slecht + "is dus niet zo erg")
        
    elif rate == array[10]:
        if slecht == "niks":
            print("Geweldig!!!")
        elif goed == "niks":
            print("waarom zei je dan dat het een slechte dag was?")
    elif rate == "12345678910":
        print("Haha jij bent grappig")
        back2 = True
    elif rate == "^^":
        print("Haha jij bent grappig")
        back2 = True
    else:
        back2 = True
        print("sorry maar ik kan alleen maar antwoord geven op 12345678910 ")