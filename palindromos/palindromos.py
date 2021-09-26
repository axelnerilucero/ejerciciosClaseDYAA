
franja=[]


def reloj():
    minutos = int(0)
    horas = int (0)

    while(horas <=23 and minutos<=60):

        hora = str(horas)
        minuto = str(minutos)
        hora_completa1 = hora.zfill(2)+":"+minuto.zfill(2)

        minutos = minutos + 1

        if (minutos==60):
            minutos=0
            horas = horas + 1
            if (horas==24):
                horas==0
        franja.append(hora_completa1)



def palindromo():
    reloj()
    for e in franja:
        if e == e[::-1]:
            print(str(e)+" Es palindromo")


palindromo()
