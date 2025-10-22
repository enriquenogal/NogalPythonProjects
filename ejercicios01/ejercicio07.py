def calcula_puntuacion(str):
    min = "abcdefghijklmnopqrstuvwxyz"
    may = min.upper()
    puntuacion = 0
    for c in str:
        try:
            puntuacion += min.index(c) + 1
        except:
            None
        try:
            puntuacion += may.index(c) + 1
        except:
            None
    return puntuacion

def calcula_ganadora(l):
    maximo = 0
    ganadora = ""
    for str in l:
        puntos = calcula_puntuacion(str)
        if (puntos > maximo):
            ganadora = str
            maximo = puntos
    return (ganadora,maximo)
    
if __name__ == "__main__": 
    maxima = 0
    ganadora_final = ""
    texto = ""
    while texto.upper() != "FIN":
        texto = ""
        while texto == "":
            texto = input("Introduce un texto: ")
        if texto.upper() != "FIN":
            l = texto.split(" ")
            tupla = calcula_ganadora(l)
            palabra_ganadora = tupla[0]
            puntuacion_ganadora = tupla[1]
            print(f"La palabra con mayor puntuación es {palabra_ganadora} y su puntuacion es {puntuacion_ganadora}")
            if (maxima < puntuacion_ganadora):
                ganadora_final = palabra_ganadora
                maxima = puntuacion_ganadora
    print(f"La ganadora entre las ganadoras es {ganadora_final} y su puntuacion es {maxima}")
# end main