import math

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
            
# def contador_cifras(n):
#    r = 0
#    while n != 0:
#        r += 1
#        n = n // 10
#    return r

contador_cifras = lambda n : int(math.log(n,10)) + 1

if __name__ == "__main__":
    n = 1
    n_cifras = 0
    max = 0
    winner = 0
    while n != 0:
        n = pedir_numero_entero_positivo()
        if n != 0:
            n_cifras = contador_cifras(n)
            print(f"{n} tiene {n_cifras} cifras")
            if n_cifras > max:
                max = n_cifras
                winner = n
    print(f"El número con más cifras es el {winner} que tiene {max} cifras")
# end main