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
            
def suma_cifras(n):
    suma = 0
    while n != 0:
        suma += n % 10
        n = n // 10
    return suma

def es_bonito(n):
    if n < 10000 or n > 99999:
        return False
    if n % 10 == 0:
        return False
    if n % 100 == 13:
        return False
    if suma_cifras(n) % 10 != 0:
        return False
    return True

if __name__ == "__main__":
    n = -1
    cont = 0
    while n != 0:
        n = pedir_numero_entero_positivo()
        if n != 0:
            if es_bonito(n):
                print("Es bonito")
                cont += 1
            else:
                print("No es bonito")
    print("Adiós!!!")
    print(f"Has introducido {cont} numeritos bonitos")
# end main