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

def lista_factores_primos(n):
    l = []
    for i in range(2, n + 1):
        while n % i == 0:
            l = l + [i]
            n = n // i
            if n == 1:
                return l

if __name__ == "__main__":
    n = -1
    while n != 0:
        n = pedir_numero_entero_positivo()
        if n != 0:
            print("Factores primos:", lista_factores_primos(n))
    print("Adiós!!!")
# end main