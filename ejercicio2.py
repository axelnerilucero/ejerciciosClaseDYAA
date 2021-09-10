import random

def puntaje(rondas):
    count = 0
    puntajes_posibles1 = ["15","30","40", "deuce", "advantage", "ganaste"]
    puntajes_posibles2 = ["15","30","40", "deuce", "advantage", "ganaste"]

    while count < rondas:# or (puntajes_posibles1[5] == "ganaste" or puntajes_posibles2[5] == "ganaste"):
        print("ronda"+str(count)+"\n")
        jugador = random.randint(1,2)
        if jugador == 1:
            print("jugador 1: "+puntajes_posibles1[0]+" --- jugador 2: "+puntajes_posibles2[1])
            puntajes_posibles1[0] = puntajes_posibles1[1]
            puntajes_posibles1[1] = puntajes_posibles1[2]
            puntajes_posibles1[2] = puntajes_posibles1[3]
            puntajes_posibles1[3] = puntajes_posibles1[4]
            puntajes_posibles1[4] = puntajes_posibles1[5]
        else:
            print("jugador 1: "+puntajes_posibles1[0]+" --- jugador 2: "+puntajes_posibles2[2])
            puntajes_posibles2[0] = puntajes_posibles2[1]
            puntajes_posibles2[1] = puntajes_posibles2[2]
            puntajes_posibles2[2] = puntajes_posibles2[3]
            puntajes_posibles2[3] = puntajes_posibles2[4]
            puntajes_posibles2[4] = puntajes_posibles2[5]

        count += 1


puntaje(13)
