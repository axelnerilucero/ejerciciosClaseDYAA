import re
# Solamente decifrar {encripatdo esta mal dicho}
cifrado ='zg gzhv lpz vidhv v gv pidqzmndyvy ivxdjivg, kjm hd mvuv cvwgvmá zg znkímdop, mzqzgv gv qjxvxdói cphviínodxv xji gv lpz apz xjixzwdyv. zg vpojm yz znov xégzwmz amvnz, ejné qvnxjixzgjn, vnphdó gv mzxojmív zi 1920, zi piv ékjxv zi lpz gvn znkzmviuvn yz gv mzqjgpxdói vúi znovwvi qdqvn, cvwív piv bmvi aé zi gv kvomdv t zg áidhj mzyziojm nz zsoziyív zi zg vhwdzioz.'
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
llave = 5
longitud = len(cifrado)
palabras = []
frases = []
for llave in range(1,len(alfabeto)):
  for i in range(len(cifrado)):
    if (cifrado[i] in alfabeto):
      index = alfabeto.index(cifrado[i])
      num = alfabeto[(index + llave) %26]
      palabras.append(num)
    else:
      num2 = cifrado[i]
      palabras.append(num2)

mensaje = lambda palabras, longitud : [palabras[i:i+longitud] for i in range(0, len(palabras), longitud)]
listaaux = mensaje(palabras, longitud)

for i in listaaux:
    frase = "".join(i)
    frases.append(frase)

def consonantes_juntas(lista, juntas):
    tres = juntas * "[bcdfghjklmnpqrstvwxyz]"

    for frase in lista:
        if re.search(tres, frase, re.IGNORECASE):
            pass
        else:
            print(frase)
consonantes_juntas(frases,3)
