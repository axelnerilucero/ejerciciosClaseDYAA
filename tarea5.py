
def calcular_monto():
    monto = input("\nIngresa el monto que deseas calcular: ")
    monto = int(monto)
    count = 0
    while monto > 0 and count < 1:
        print(f"\nTu monto es: {monto}")
        if monto > 999:
            quinientos = (monto-(monto%500))/500
            rq = monto-(quinientos*500)

        quinientos = (monto-(monto%500))/500
        rq = monto-(quinientos*500)

        if rq >= 200 or monto >= 200:
            docientos = (rq-(rq%200))/200
            rd = rq-(docientos*200)

        docientos = (rq-(rq%200))/200
        rd = rq-(docientos*200)

        if rd >= 100 or monto >= 100:
            cien = (rd-(rd%100))/100
            rc = rd-(cien*100)

        cien = (rd-(rd%100))/100
        rc = rd-(cien*100)

        if rc >= 20 or monto >= 20:
            veinte = (rc-(rc%20))/20
            rv = rc-(veinte*20)
        veinte = (rc-(rc%20))/20
        rv = rc-(veinte*20)

        if rv >= 10 or monto >= 10:
            diez = (rv-(rv%10))/10
            rdi = rv-(diez*10)

        diez = (rv-(rv%10))/10
        rdi = rv-(diez*10)

        if rdi >= 5 or monto >= 5:
            cinco = (rdi-(rdi%5))/5
            rci = rdi-(cinco*5)

        cinco = (rdi-(rdi%5))/5
        rci = rdi-(cinco*5)

        if rci >= 1 or monto >= 1:
            uno = (rci-(rci%1))/1
            ru = rci-(uno*1)

        uno = (rci-(rci%1))/1
        ru = rci-(uno*1)

        if ru >= 0.5 or monto >= 0.5:
            cincuenta = (ru-(ru%0.5))/0.5
            rcin = ru-(cincuenta*0.5)

    # mostrar la cantidad de cada denominacion con la que se cuenta

        if quinientos < 0:
            print(f"No cuentas con billetes de quinientos")
        else:
            print(f"Tienes {int(quinientos)} biletes de quinientos")
        if docientos <= 0:
            print(f"No cuentas con billetes de docientos")
        else:
            print(f"Tienes {int(docientos)} billetes de docientos")
        if cien <= 0:
            print(f"No cuentas con billetes de cien")
        else:
            print(f"Tienes {int(cien)} billetes de cien")
        if veinte <= 0:
            print(f"No cuentas con monedas de veinte")
        else:
            print(f"Tienes {int(veinte)} monedas de veinte")
        if diez <= 0:
            print(f"No cuentas con monedas de diez")
        else:
            print(f"Tienes {int(diez)} monedas de diez")
        if cinco <= 0:
            print(f"No cuentas con monedas de cinco")
        else:
            print(f"Tienes {int(cinco)} monedas de cinco")
        if uno <= 0:
            print(f"No cuentas con monedas de uno")
        else:
            print(f"Tienes {int(uno)} monedas de uno")
        if cincuenta <= 0:
            print(f"No cuentas con monedas de cincuenta centavos")
        else:
            print(f"Tienes {int(cincuenta)} monedas de cincuenta centavos")
        count +=1
        print("\n\n")
    #print("Ingresa un numero valido")


def menu():
    opc = 0
    while (opc !=1):
        print ("1. Salir")
        print ("2. Calcular denominaciones del monto")
        opc = int(input("\nDame opcion: "))
        if (opc == 2):
            calcular_monto()

menu()
