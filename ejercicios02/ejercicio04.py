def pedir_numero_entero_positivo():
    while True:
        try:
            str = input("Dame un numero entero positivo: ")
            n = int(str)
        except:
            print("Eso no es un número entero")
        else:
            if n < 0:
                print("Debería ser positivo")
            else:
                return n

def menor_mayor(numero):
    cadena_numero = str(numero)
    lista_cifras_ordenadas_ascendente = sorted(cadena_numero)
    cadena_ordenada_ascendente = "".join(lista_cifras_ordenadas_ascendente)
    lista_cifras_ordenadas_descendente = sorted(cadena_numero, reverse = True)
    cadena_ordenada_descendente = "".join(lista_cifras_ordenadas_descendente)
    menor = int(cadena_ordenada_ascendente)
    mayor = int(cadena_ordenada_descendente )
    return (menor,mayor)

if __name__ == "__main__":
    n = -1
    while n != 0:
        n = pedir_numero_entero_positivo()
        if n != 0:
            print("Salida: ")
            t = menor_mayor(n)
            print(f" - Número mayor: {t[1]}")
            print(f" - Número menor: {t[0]}")
            resta = t[1] - t[0]
            print(f" - Resultado de la resta: {resta}")
            if resta % 9 == 0:
                print(f" - ¿{resta} es divisible entre 9? si")
            else:
                print(f" - ¿{resta} es divisible entre 9? no")
    print("----------------")
    for i in range(1,1000001):
        t = menor_mayor(i)
        if (t[1] - t[0]) % 9 != 0: print(i)

# end main