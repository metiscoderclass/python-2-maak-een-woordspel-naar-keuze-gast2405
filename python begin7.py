back = True
lijst = ["ja", "nee", "mischien"]
while back == True:
    back = False
    vraag = input("stel mij een vraag.")
    if vraag == " ben jij gay":
        print("nee maar jij wel")
        back = True
    elif vraag == "is jonas gay":
        print("ja op jou")
        back = True
    elif vraag == "is anuar gay":
        print("nee hij is transgender")
        back = True
    elif vraag == "mag ik jouw computer hacken":
        print("ja mijn code is '1683' L.O.L dat is niet echt. ")
        back = True
    elif vraag == "hou je überhaupt wel van ananas":
        print("ja en ik denk jij ook")
        back = True
    elif vraag == "hoe was je dag":
        dag = input("goed en hoe was jouw dag")
        back = True
    elif vraag == "hoeveel boswervels heeft een mens":
        print("12")
        back = True
    elif vraag == "wat is je favoriete liedje":
        print("i am sexy and i know it")
        back = True
    elif vraag == "met hoeveel mensen woon je in huis":
        print("0 mensen maar 2 robots")
        back = True
    elif vraag == "wat is de bedoeling van het leven":
        print("42")
        back = True
    elif vraag == "waarom is pablo suicidaal":
        print("omdat hij jouw gezicht zag")
        back = True
    elif vraag == "waar ben je":
        print("overal en nergens")
        back = True
    elif vraag == "ben je lelijk":
        print("ja maar dat komt omdat mijn gezicht smelte toen het jouw lelijke gezicht zag")
        back = True
    elif vraag == "wat vind je van de politiek":
        print("dat het stom is")
        back = True
    elif vraag == "wat is beter apple of samsung":
        print("samsung en apple zijn gay")
        back == True
    else:
        import random
        random = random.choice(lijst)
        print(random)
        back = True