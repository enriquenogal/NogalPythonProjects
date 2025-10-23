import sys

def cifrar(claro,clave):
    texto_cifrado = ""
    min = "abcdefghijklmnñopqrstuvxyz"
    may = min.upper()
    posicion = 0
    i = 0
    for c in texto_claro:
        if c in min:
            posicion = (min.index(c) - min.index(clave[i])) % len(min)
            texto_cifrado += min[posicion]
            i = (i + 1) % len(clave)
        elif c in may:
            posicion = (may.index(c) - min.index(clave[i])) % len(min)
            texto_cifrado += may[posicion]
            i = (i + 1) % len(clave)
        else:
            texto_cifrado += c
    return texto_cifrado

if __name__ == "__main__":
    texto_claro = ""
    clave = ""
    texto_cifrado = ""
    if len(sys.argv) != 3:
        #sys.exit("Número de parámetros incorrecto")
        texto_claro = input("Dame el texto a descifrar: ")
        clave = input("Dame la clave de cifrado que se utilizó: ").lower().replace(" ", "")
    else:
        texto_claro = sys.argv[1]
        clave = sys.argv[2].lower().replace(" ", "")

    texto_cifrado = cifrar(texto_claro,clave)
    print(texto_cifrado)

# end main
