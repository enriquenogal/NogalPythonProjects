
#tuplas paréntesis ()
#listas corchetes []

if __name__ == "__main__":
    print("hola")
    # tuplas
    # inmutables - no se pueden modificar los valores de las posiciones
    var_tupla = () #inicialización que puedes no hacer
    var_tupla = (1,"pepe",3.14) #inicialización/asignación
    var_tupla = var_tupla + (8,9)
    for i in range(len(var_tupla)):
        print(var_tupla[i])
    for item in var_tupla:
        print(item)

    print(var_tupla[1:3])    

    # var_tupla[2] = 9 # arroja un error pues no se pueden modificar valores

    # se usan para hacer swap de valores de dos variables
    x = 1
    y = 3
    print("x: " , x , " y: " , y)
    (x,y) = (y,x)
    print("x: " , x , " y: " , y)

    # se pueden hacer multidimensionales
    var_tupla_dos_dimensiones = ((1,2,3),(4,5,6),(7,8,9))
    for item1 in var_tupla_dos_dimensiones:
        for item2 in item1:
            print(item2, end=" ")
        print()

    # listas
    # estas si que son mutables
    var_list = [] #inicialización
    var_list = [1,"pepe",3.14] #inicialización/asignación
    var_list = var_list + [5,6]
    for i in range(len(var_list)):
        print(var_list[i])
    for item in var_list:
        print(item)

    var_list[2] = 9 # esto si que funciona al ser mutables los objetos de las posiciones del list
    
    # además se pueden aplicar algunas funciones gracias a la mutabilidad
    #inserciones
    var_list.append("hola")
    var_list.extend([99,99,100])
    var_list.insert(1, "orange")
    print(var_list)
    #borrados
    del(var_list[2]) # borra la posición del índice que has marcado 
    print(var_list)
    print(var_list.pop()) # borra la última posición y te devuelve el valor que estuviera almacenado
    print(var_list.pop(0)) # borra la posición del índice y te devuelve el valor que estuviera almacenado
    var_list.remove(99) # borra la primera ocurrencia con valor 99. Si no lo encontrase muestra un error
    print(var_list)
    var_list.clear() # borra la lista completa
    print(var_list)

    # string a listas y viceversa
    str1 = "hola pepe"
    l1 = list(str1)
    print(l1)
    l2 = str1.split(" ")
    print(l2)
    l3 = ["a","b","c"]
    str2 = "".join(l3)
    print(str2)
    str2 = " ".join(l3)
    print(str2)

    #ordenaciones
    l4 = [3,4,1,8,4,1,2,0]
    l5 = sorted(l4) #devuelve una lista ordenada pero no muta la lista l4 original
    print("l4 = " , l4)
    print("l5 = " , l5)
    l4.sort() #muta la lista ordenándola
    print("l4 = " , l4)
    l5.reverse() #muta la lista ordenándola descendentemente
    #l5.sort(reverse = True) #muta la lista ordenándola descendentemente
    print("l5 = " , l5)

    #cuidado con los punteros
    var1 = 1
    var2 = var1
    print(var1, var2)
    var2 = 8
    print(var1, var2)
    #pero esto con una lista no es así
    l1 = [0,1,2]
    l2 = l1
    print(l1, l2)
    l2.append(3)
    print(l1, l2) #no sólo se ha modificado l2 sino que también l1
    #así que quizás lo que necesites es clonar para no ocurra esto
    l1 = [0,1,2]
    l2 = l1[:] #así estás asignando los valores que hay desde la posición 0 hasta len-1 de l1
    print(l1, l2)
    l2.append(3)
    print(l1, l2)

    # extras
    lista_numeros = [7,2,3,4,56,1,2,44,56]
    print(sum(lista_numeros))
    print(max(lista_numeros))
    print(min(lista_numeros))
    print(sum(lista_numeros)/len(lista_numeros))

    # para saber si contiene o no un valor
    if 56 in lista_numeros:
        print("el 56 está")

    # otro modo de recorrer
    nombres = ["Ana", "Luis"]
    [print(nombre) for nombre in nombres]

# end main