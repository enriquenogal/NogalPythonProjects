if __name__ == "__main__":
    # Los elementos de un set son únicos, lo que significa que no puede haber elementos duplicados.
    # Los set son desordenados, lo que significa que no mantienen el orden de cuando son declarados.
    # Sus elementos son inmutables.
    set01 = {4,6,1,"pepe"}
    set02 = {10,6,8}
    for elemento in set01:
        print(elemento) 
    
    # print(set01[0]) # no funciona, no se puede acceder a las posiciones del set con los corchetes
    # set01 = set01 + set02 # no funciona, no se comporta del todo como las listas o las tuplas
    set01 = set01.union(set02) # para hacerlo necesitas recurrir al método union
    print(set01)

    # así puedes añadir un elemento, aunque en este caso no se añadirá al estar ya anteriormente
    # los repetidos no se insertarán
    set01.add(1)
    print(set01)

    # hay más métodos interesantes
    print(set01.intersection(set02))
    print(set01.difference({4,5}))
    print({4,5}.difference(set01))

    # El método remove() elimina el elemento que se pasa como parámetro. Si no se encuentra, se lanza la excepción KeyError.
    # El método discard() es muy parecido al remove(), borra el elemento que se pasa como parámetro, y si no se encuentra no hace nada.
    # El método pop() elimina un elemento aleatorio del set.
    # El método clear() elimina todos los elementos de set.
    
# end main