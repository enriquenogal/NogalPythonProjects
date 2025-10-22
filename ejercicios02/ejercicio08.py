if __name__ == "__main__":
    n = int(input("Nº de puntuaciones:"))
    arr = map(int, input("Puntuaciones separadas por un espacio: ").split())

    lista = list(arr)
    maximo = max(lista)
    while maximo in lista:
        lista.remove(maximo)

    if len(lista) > 0:    
        print("Calificación segunda del ranking: ",max(lista))
    else:
        print("No hay segundas calificaciones en el ranking")
# end main