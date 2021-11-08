"""
def calcular(numero):
    numeros = []
    numero += 1
    while numero > 0:
        numero  = numero - 1
        numeros.append(numero)
    print(numeros)
    numero = numero -1
    suma = sum(numeros)
    print(suma)
calcular(3)
"""
"""
def listan1er(lista):
    lista2 = lista.copy()
    combinaciones = [(x,y) for x in lista for y in lista2]
    print("Entrada: "+str(lista))
    print(combinaciones)
    print("Final: "+str(len(combinaciones)))

a = [1,2,3]
tab = listan1er(a)


def listan2do(lista):
    lista2 = lista.copy()
    combinaciones = [(x,y) for x in lista for y in lista2]
    print("Entrada: "+str(lista))
    for elem in combinaciones:
        print(elem)
    print("Final: "+str(len(combinaciones)))

a = [1,2,3]
tab = listan2do(a)
"""

def listan(lista):
    lista2 = lista.copy()
    combinaciones = [(x,y) for x in lista for y in lista2]
    print("Entrada: "+str(lista))
    for elem in combinaciones:
        print(elem)
    print("Final: "+str(len(combinaciones)))

a = [1,2,3]
tab = listan(a)
