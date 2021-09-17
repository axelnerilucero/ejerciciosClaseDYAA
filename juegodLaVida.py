
class matriz:
    viva = 1
    muerta = 0
    def __init__(self, ren, col, valor):
        self.__ren = ren
        self.__col = col
        self.__array = [[valor for x in range(self.__col+2)] for y in range(self.__ren+2)]


    def numeroren(self):
        return self.__ren

    def numerocol(self):
        return self.__col

    def getItem(self, ren, col):
        return self.__array[ren][col]

    def setItem(self, ren, col, valor):
        self.__array[ren][col] = valor

    def limpiar(self, valor = 0):
        for reng in range(self.__ren):
            for cols in range(self.__col):
                self.__array[reng][cols] = valor

    def tablero(self):
        for r in range(1,self.numeroren()+1):
            for c in range(1,self.numerocol()+1):
                if self.getItem(r,c) == 0:
                    print(" 0 ", end="")
                else:
                    print(" 1 ", end="")
            print("")


    def generacion1(self, poblacion):
        self.limpiar()
        for celula in poblacion:
            self.setItem(celula[0], celula[1], self.viva)


    def ejecucion(self, generaciones):
        count = 1
        while count <= generaciones:
            for r in range(1,self.numeroren()+1):
                for c in range(1,self.numerocol()+1):
                    vecinos = self.getItem(r,c+1) + self.getItem(r,c-1) + self.getItem(r-1,c) \
                            + self.getItem(r+1,c) + self.getItem(r-1,c-1) + self.getItem(r+1,c-1) \
                            + self.getItem(r-1,c+1) + self.getItem(r+1,c+1)
                    if self.getItem(r,c) == 1 and vecinos == 2:
                        self.setItem(r, c, self.viva)

                    elif self.getItem(r,c) == 1 and vecinos == 3:
                        self.setItem(r, c, self.viva)

                    elif self.getItem(r,c) == 1 and vecinos == 0:
                        self.setItem(r, c, self.muerta)

                    elif self.getItem(r,c) == 1 and vecinos == 1:
                        self.setItem(r, c, self.muerta)

                    elif self.getItem(r,c) == 1 and vecinos >= 4:
                        self.setItem(r, c, self.muerta)

                    elif self.getItem(r,c) == 0 and vecinos == 3:
                        self.setItem(r, c, self.viva)

                    elif self.getItem(r,c) == 0 and vecinos < 3:
                        self.setItem(r, c, self.muerta)




            self.tablero()
            print("\n")
            count = count + 1
        print("ya acabo las "+ str(generaciones))


tab = matriz(6,5,0)
tab.tablero()
print("-----------------------")
tab.generacion1([(3,2),(3,3),(3,4),(4,2),(4,4),(5,2),(5,3),(5,4)])
tab.tablero()
print("\n")
tab.ejecucion(10)
