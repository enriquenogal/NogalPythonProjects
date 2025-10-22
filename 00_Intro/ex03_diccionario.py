# diccionarios llaves {} y dentro separas con : la clave del valor
# dict = {"R. Madrid" : 15, "Barcelona" : 5, "Atleti" : 0}


def factorial_recursivo(n):
    """
    Purpose: arg
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)
# end def
    



if __name__ == "__main__":
    print("ex03")
    print("factorial de 5: ",factorial_recursivo(5))

    dict={} # #inicialización que puedes no hacer
    dict = {"R. Madrid" : 15, "Barcelona" : 5, "Atleti" : 0} #inicialización/asignación
    print(dict["R. Madrid"])
    dict["R. Madrid"] = 16
    print(dict["R. Madrid"])
    dict["Leganés"] = 1 # añadir una entrada con clave Leganés y valor 1
    print(dict["Leganés"])
    del(dict["Atleti"]) # borrar la entrada con clave Atleti
    if "Atleti" in dict:
        print("El Atleti si está entre los ganadores de Champions")
    else:
        print("El Atleti no está entre los ganadores de Champions")
    print("---------------Sin Orden-----------------")
    for key in dict.keys():
        print(key, dict[key])
    print("---------------Ordenados-----------------")
    for key in sorted(dict.keys()):
        print(key, dict[key])

    dict["Leganés"] = dict["Leganés"] + 15
    mejores = []
    valores = dict.values()
    best = max(valores)
    for key in dict.keys():
        if dict[key] == best:
            mejores = mejores + [key]
    print("Mejores:", mejores)

    dict.clear()
    print(len(dict))



# end main