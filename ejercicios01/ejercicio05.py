def pedir_numero_entero_positivo():
    while True:
        try:
            str = input("Dame un numero entero positivo: ")
            n = int(str)
        except:
            print("Eso no es un número entero")
        else:
            if n <= 0:
                print("Debería ser mayor de cero")
            else:
                return n

def es_correcta(l):
    for i in range (1, len(l)):
        if (l[i][0] != l[i-1][1]):
            return False
    return True

if __name__ == "__main__":
    l = []
    dic = {}
    n_fichas = 0
    print("Dime el número de fichas que hay en la mesa.", end = " ")
    n_fichas = pedir_numero_entero_positivo()
    for i in range(1, n_fichas+ 1):
        print(f"Información de la ficha {i}")
        inicio = input(" - Dime el número de puntos que hay en la primera mitad de la ficha: ")
        fin = input(" - Dime el número de puntos que hay en la segunda mitad de la ficha: ")
        l.append((inicio,fin))
        ficha = min(inicio,fin) + "-" + max(inicio,fin)
        dic[ficha] = dic.get(ficha,0) + 1
    if (es_correcta(l)):
        print("CORRECTO")
    else:
        print("ERROR")
    print(f"Hacen falta {max(dic.values())} cajas de fichas para esta partida")
# end main