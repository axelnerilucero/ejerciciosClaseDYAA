f = open('el_quijote_ii.txt','r',encoding="utf8")
A = f.read()
resultados = []
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
            resultados.append(i)

    print(f"con la palabra {P} se encontraron {count} coincidencias en las siguientes posiciones {resultados}")
    resultados.clear()

entrada = "0011100101011011101"
patron = ["molino", "hidalgo", "merced"]
for i in patron:
    string_match_brute(A,i)
