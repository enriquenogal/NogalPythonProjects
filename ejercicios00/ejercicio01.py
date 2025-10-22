import sys

if __name__ == "__main__":
    dato = "NO FIN"
    suma = 0
    contador = 0
    max = -sys.maxsize - 1
    min = sys.maxsize

    while dato.upper() != "FIN":
        dato = input("Dame un número: ")
        if dato.upper() != "FIN":
            try:
                numero = int(dato)
                suma += numero
                contador += 1
                if numero > max:
                    max = numero
                if numero < min:
                    min = numero
            except:
                print("Eso no era un número")
    media = suma / contador
    print("máximo:", max)
    print("mínimo", min)
    print("suma:", suma)
    print("número de elementos:",contador)
    print("media:", media)
# end main