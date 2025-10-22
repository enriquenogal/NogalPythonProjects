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

contador_cifras = lambda n : int(math.log(n,10)) + 1

def es_tonteria(n):
    r = 0
    inicio = n
    cifras = contador_cifras(n)
    while n != 0:
        r += (n % 10) ** cifras
        n = n // 10
        cifras -= 1
    if r == inicio: return True
    return False

def lista_tonteria(inicio, fin):
    l = []
    for i in range (inicio, fin + 1):
        if es_tonteria(i):
            l += [i]
    return l

if __name__ == "__main__":
    inicio = 0
    fin = 1
    while inicio <= fin:
        inicio = pedir_numero_entero_positivo()
        fin = pedir_numero_entero_positivo()
        if inicio <= fin:
            print(lista_tonteria(inicio,fin))