import sys

def cifrar(claro,clave):
    texto_cifrado = ""
    min = "abcdefghijklmnñopqrstuvxyz"
    may = min.upper()
    posicion = 0
    cifrada = False
    i = 0
    for c in texto_claro:
        cifrada = False
        try:
            posicion = (min.index(c) - min.index(clave[i])) % len(min)
            texto_cifrado += min[posicion]
            cifrada = True
            i = (i + 1) % len(clave)
        except:
            None
        try:
            posicion = (may.index(c) - min.index(clave[i])) % len(min)
            texto_cifrado += may[posicion]
            cifrada = True
            i = (i + 1) % len(clave)
        except:
            None
        if not(cifrada):
            texto_cifrado += c
    return texto_cifrado

if __name__ == "__main__":
    texto_claro = ""
    clave = ""
    texto_cifrado = ""
    if len(sys.argv) != 3:
        #sys.exit("Número de parámetros incorrecto")
        texto_claro = "Hplb eqeA"
        clave = "ab"
    else:
        texto_claro = sys.argv[1]
        clave = sys.argv[2].lower()

    texto_cifrado = cifrar(texto_claro,clave)
    print(texto_cifrado)

# end main
