# posibles sonrisas :) :D ;) ;D :-) :~) ;-) ;~D

def countSmileys(str):
    contador = 0
    for i in range(len(str)):
        if str[i : i + 2] in (":)",":D",";)",";D"):
            contador += 1
        if str[i : i + 3] in (":-)",":~)",";-)",";~D"):
            contador += 1
    return contador

if __name__ == "__main__":
    maxima = 0
    ganadora_final = ""
    texto = ""
    while texto.upper() != "FIN":
        texto = ""
        while texto == "":
            texto = input("Introduce un texto: ")
        if texto.upper() != "FIN":
            contador = countSmileys(texto)
            print(f"La cantidad de sonrisas en ese texto es de {contador}")
            if contador > maxima:
                maxima = contador
                ganadora_final = texto
    print(f"El texto con mayor número de sonrisas es {ganadora_final} que tiene {maxima} sonrisas")

# end main