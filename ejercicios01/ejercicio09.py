import sys

def pedir_numero_entero_mayor_de_cero():
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
            
def cumple(dic):
    diferencia_anterior = sys.maxsize
    for key in sorted(dic.keys()):
        diferencia = dic.get(key) - key
        if diferencia >= diferencia_anterior:
            return False
        else:
            diferencia_anterior = diferencia
    return True
# end def

if __name__ == "__main__":
    print("Dime el número de personas que participan en el estudio.", end = " ")
    numero_personas = pedir_numero_entero_mayor_de_cero()
    dic = {}
    for i in range(1,numero_personas + 1):
        print(f"Dame los datos de la persona {i} participante en el estudio")
        print("   - Percepción propia.", end = " ")
        percepcion_propia = pedir_numero_entero_positivo()
        print("   - Examen de evaluación.", end = " ")
        examen_evaluacion = pedir_numero_entero_positivo()
        dic[examen_evaluacion] = percepcion_propia
    if cumple(dic):
        print("SI")
    else:
        print("NO")
# end main