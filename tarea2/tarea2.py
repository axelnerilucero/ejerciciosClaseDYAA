
class lista:
    def __init__(self, arr):
        arr = []

    def agregar(self, numero):
        if numero in arr :
            print("no se puede agregar el numero "+str(numero)+" porque ya existe")
        else:
            arr.append(numero)
            for r in range(len(arr)):
                for j in range(r,0,-1):
                    if arr[j-1] > arr[j]:
                        aux = arr[j]
                        arr[j] = arr[j-1]
                        arr[j-1] = aux

    def busqueda(self, numero):
        i=0
        if numero in arr:
            for z in arr:
                if z == numero:
                    print("el numero "+str(numero)+" existe en la posicion "+str(i+1))
                else:
                    i=i+1


        else:
            print("el numero "+str(numero)+" no existe")


arr = [2,4]
tab = lista(arr)
tab.agregar(3)
tab.agregar(5)
tab.agregar(9)
tab.agregar(52)
tab.agregar(5)
print(arr)
tab.busqueda(2)
tab.busqueda(9)
tab.busqueda(52)
tab.busqueda(345)
