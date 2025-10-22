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

def factorial(n):
    if n == 0: return 1
    if n == 1: return 1
    r = 1
    for i in range (2, n + 1):
        r *= i
    return r

def es_peterson(n):
    r = 0
    inicio = n
    while n != 0:
        r += factorial(n % 10)
        n = n // 10
    if r == inicio: return True
    return False

def lista_peterson(inicio, fin):
    l = []
    for i in range (inicio, fin + 1):
        if es_peterson(i):
            l += [i]
    return l

if __name__ == "__main__":
    inicio = 0
    fin = 1
    while inicio <= fin:
        inicio = pedir_numero_entero_positivo()
        fin = pedir_numero_entero_positivo()
        if inicio <= fin:
            print(lista_peterson(inicio,fin))
# end main