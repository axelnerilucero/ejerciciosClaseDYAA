f = open('el_quijote_ii.txt','r',encoding="utf8")
A = f.read()
def string_match_brute(A,P):
    count = 0
    for i in range(len(A) - len(P) + 1):
        for j in range(len(P)):
            if P[j] == A[i+j]:
                pass
            else:
                break
        if j+1 == len(P) and A[i+j] == P[j]:
            count = count + 1
            print(f"Palabra {P} encontrada en la posicion {i}")
    print(f"con la palabra {P} se encontraron {count} coincidencias")

entrada = "0011100101011011101"
patron = ["molino", "hidalgo", "merced"]
for i in patron:
    string_match_brute(A,i)
