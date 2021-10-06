
def calcular_monto():
    monto = input("\nIngresa el monto que deseas calcular: ") # O(39) O(1)
    monto = int(monto) # O(1*4) O(1)
    count = 0 # O(4) O(1)
    while monto > 0 and count < 1: # O() O()
        print(f"\nTu monto es: {monto}")
        if monto > 999: #O(0) O(na)
            quinientos = (monto-(monto%500))/500 # O(4) O(1)
            rq = monto-(quinientos*500) # O(4) O(1)

        quinientos = (monto-(monto%500))/500 # O(4) O(1)
        rq = monto-(quinientos*500) # O(4) O(1)

        if rq >= 200 or monto >= 200: #O(0) O(na)
            docientos = (rq-(rq%200))/200 # O(4) O(1)
            rd = rq-(docientos*200) # O(4) O(1)

        docientos = (rq-(rq%200))/200 # O(4) O(1)
        rd = rq-(docientos*200) # O(4) O(1)

        if rd >= 100 or monto >= 100: #O(0) O(na)
            cien = (rd-(rd%100))/100 # O(4) O(1)
            rc = rd-(cien*100) # O(4) O(1)

        cien = (rd-(rd%100))/100 # O(4) (1)
        rc = rd-(cien*100) # O(4) O(1)

        if rc >= 20 or monto >= 20: #O(0) O(na)
            veinte = (rc-(rc%20))/20 # O(4) O(1)
            rv = rc-(veinte*20) # O(4) O(1)

        veinte = (rc-(rc%20))/20 # O(4) O(1)
        rv = rc-(veinte*20) # O(4) O(1)

        if rv >= 10 or monto >= 10: #O(0) O(na)
            diez = (rv-(rv%10))/10 # O(4) O(1)
            rdi = rv-(diez*10) # O(4) O(1)

        diez = (rv-(rv%10))/10 # O(4) O(1)
        rdi = rv-(diez*10) # O(4) O(1)

        if rdi >= 5 or monto >= 5: #O(0) O(na)
            cinco = (rdi-(rdi%5))/5 # O(4) O(1)
            rci = rdi-(cinco*5) # O(4) O(1)

        cinco = (rdi-(rdi%5))/5 # O(4) O(1)
        rci = rdi-(cinco*5) # O(4) O(1)

        if rci >= 1 or monto >= 1: #O(0) O(na)
            uno = (rci-(rci%1))/1 # O4() O(1)
            ru = rci-(uno*1) # O(4) O(1)

        uno = (rci-(rci%1))/1 # O(4) O(1)
        ru = rci-(uno*1) # O(4) O(1)

        if ru >= 0.5 or monto >= 0.5:
            cincuenta = (ru-(ru%0.5))/0.5 # O(4) O(1)
            rcin = ru-(cincuenta*0.5) # O(4) O(1)

    # mostrar la cantidad de cada denominacion con la que se cuenta

        if quinientos < 0: #O(0) O(na)
            print(f"No cuentas con billetes de quinientos")
        else: #O(0) O(na)
            print(f"Tienes {int(quinientos)} biletes de quinientos")
        if docientos <= 0: #O(0) O(na)
            print(f"No cuentas con billetes de docientos")
        else: #O(0) O(na)
            print(f"Tienes {int(docientos)} billetes de docientos")
        if cien <= 0: #O(0) O(na)
            print(f"No cuentas con billetes de cien")
        else: #O(0) O(na)
            print(f"Tienes {int(cien)} billetes de cien")
        if veinte <= 0: #O(0) O(na)
            print(f"No cuentas con monedas de veinte")
        else: #O(0) O(na)
            print(f"Tienes {int(veinte)} monedas de veinte")
        if diez <= 0: #O(0) O(na)
            print(f"No cuentas con monedas de diez")
        else: #O(0) O(na)
            print(f"Tienes {int(diez)} monedas de diez")
        if cinco <= 0: #O(0) O(na)
            print(f"No cuentas con monedas de cinco")
        else: #O(0) O(na)
            print(f"Tienes {int(cinco)} monedas de cinco")
        if uno <= 0: #O(0) O(na)
            print(f"No cuentas con monedas de uno")
        else: #O(0) O(na)
            print(f"Tienes {int(uno)} monedas de uno")
        if cincuenta <= 0: #O(0) O(na)
            print(f"No cuentas con monedas de cincuenta centavos")
        else: #O(0) O(na)
            print(f"Tienes {int(cincuenta)} monedas de cincuenta centavos")
        count +=1 #O(0) O(1)
        print("\n\n")



def menu():
    opc = 0 #O(4) O(1)
    while (opc !=1):
        print ("1. Salir")
        print ("2. Calcular denominaciones del monto")
        opc = int(input("\nDame opcion: ")) #O(13) O(1)
        if (opc == 2):
            calcular_monto() #O(162) O(34)

menu()
# Memoria O(162+4+13 = 179)
# Procesamiento O(34+2 = 36)
