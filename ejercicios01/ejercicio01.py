import random

def menu_juego():
    opcion = ""
    while not(opcion == "1" or opcion == "2"):
        print("-----MENÚ-----")
        print("1. Adivina máquina")
        print("2. Adivina usuario")
        opcion = input("Introduzca una opción: ")
        if not(opcion == "1" or opcion == "2"):
            print("Opción incorrecta")
    return opcion

def menu_repetir():
    opcion = ""
    while not(opcion == "N" or opcion == "S"):
        opcion = input("¿Quiere volver a jugar (S/N)? ").upper()
        if not(opcion == "S" or opcion == "N"):
            print("Opción incorrecta")
    return opcion

def menu_mayor_menor_acierto():
    opcion = ""
    while not(opcion == "MENOR" or opcion == "MAYOR" or opcion == "ACIERTO"):
        opcion = input("¿Es MAYOR, MENOR o ACIERTO? ").upper()
        if not(opcion == "MENOR" or opcion == "MAYOR" or opcion == "ACIERTO"):
            print("Opción incorrecta")
    return opcion

def introInt():
    while True:
        n = input("Introduce un número: ")
        if n.isdigit():
            return int(n)
        else:
            print("Eso no es un número")

def adivina_maquina():
    inicio = 1
    fin = 100
    opcion = ""
    contador = 0
    input("Piensa un número que me toca adivinarlo (pulsa enter para empezar)")
    while opcion != "ACIERTO":
        contador += 1
        nMaquina = random.randint(inicio, fin)
        print("He pensado el número", nMaquina)
        opcion = menu_mayor_menor_acierto()
        if opcion == "MENOR":
            fin = nMaquina - 1
        elif opcion == "MAYOR":
            inicio = nMaquina + 1
        else:
            print("Acerté en el intento", contador)

def adivina_usuario():
    nMaquina = random.randint(1, 100)
    nUsuario = 0
    contador = 0
    print("Ya me he pensado un número del 1 al 100, a ver si lo aciertas")
    while nMaquina != nUsuario:
        contador += 1
        nUsuario = introInt()
        if nUsuario == nMaquina:
            print("Acertaste, era el número", nUsuario, "lo conseguiste en el intento", contador)
        elif nUsuario > nMaquina:
            print("ohhh... el número que he pensado es menor")
        else:
            print("ohhh... el número que he pensado es mayor")

if __name__ == "__main__":
    opcion = ""
    while opcion != "N":
        opcion = menu_juego()
        if opcion == "1":
            adivina_maquina()
        elif opcion == "2":
            adivina_usuario()
        opcion = menu_repetir()
    print("Adiós!!!")
# end main