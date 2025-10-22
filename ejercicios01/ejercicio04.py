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

nicomano = lambda n : ((n * (n + 1)) // 2) ** 2

def lista_nicomanos(n):
    l = []
    i = 1
    while True:
        tmp = nicomano(i)
        if tmp <= n:
            l.append(tmp)
            i += 1
        else:
            break
    return l

if __name__ == "__main__":
    n = -1
    while n != 0:
        n = pedir_numero_entero_positivo()
        if n != 0:
            print("Lista de números de Nicómano:", lista_nicomanos(n))
    print("Adiós!!!")
# end main