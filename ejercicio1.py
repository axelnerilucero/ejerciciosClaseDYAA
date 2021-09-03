telefono = ["2563 26 51 63", "643 256 48 32", "321 3522 131 3",  "12345678912", "4562 5 5 3269", "7555 123456", "45 26 5 2 4 3 6 3", "4 121 56 624 "]

def numero_completo():

    for i in telefono:
        e = i.replace(" ","")
        if len(e) == 10:
            print(i+" ==> "+"+52"+e+"\n")
        elif len(e) < 10:
            print("un numero telefonico no cumple con los 10 digitos"+"\n")
        else:
            print("un numero telefonico excede los 10 digitos"+"\n")

numero_completo()
