class Automovil():

    def __init__(self, velocidad, llantas, puertas, asientos, seguro, encendido):
        self.velocidad = velocidad = 0
        self.llantas = llantas = 4
        self.puertas = puertas = 4
        self.asientos = asientos = 4
        self.seguro = seguro = False
        self.encendido = encendido = False

    def encender(self):
        encendido = True
        return "El_vehiculo_esta_ON"

    def acelerar(self):
        for Rapidez in range(0, 104, 5):
            print(f"el vehiculo esta moviendose a {Rapidez} km/h")

        return "El_vehiculo_esta_moviendose"

    def frenar(self):
        velocidad = 100
        while(velocidad >= 0):
            print("velocidad:" , velocidad)
            velocidad -= 10
        return "El_vehiculo_esta_deteniendose"

    def apagar(self):
        encendido = False
        return "El_vehiculo_esta_OFF"

    def modificar_estado(self):
        if self.encendido == False:
            self.encender()
        elif self.encendido == True :
            self.apagar()

nuevoAuto = Automovil(0, 4, 4, 4, False, False)
print(nuevoAuto.modificar_estado())
print(nuevoAuto.acelerar())
print(nuevoAuto.frenar())
print(nuevoAuto.apagar())
#
