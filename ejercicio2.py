import random

def puntaje():
    for x in range(10):
        jugador = random.randint(1,2)
        pun1 = 0
        pun2 = 0
        if jugador == 1:
            pun1 = 15
            if pun1 == 15:
                pun1 = 30
                if pun1 == 30:
                    pun1 = 40
                    if pun1 == 40:
                        pun1 = "ganaste"

        else:
            pun2 = 15
            if pun2 == 15:
                pun2 = 30
                if pun2 == 30:
                    pun2 = 40
                    if pun2 == 40:
                        pun2 = "ganaste"
        if pun1 and pun2 == "ganaste":
            pun1 and pun2 == "deuce"
        print("jugador 1: "+ str(pun1) + " ----------- "+"jugador 2: "+ str(pun2))
puntaje()
