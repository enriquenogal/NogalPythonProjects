def busca_indice(l):
    print(l)
    for i in range(len(l)):
        if sum(l[:i]) == sum(l[i:]):
            return i
    return -1    
# end def

if __name__ == "__main__":
    dato = "NO FIN"
    l = []
    while dato.upper() != "FIN":
        dato = input("Dame un número: ")
        if dato.upper() != "FIN":
            try:
                l.append(int(dato))
            except:
                print("Eso no era un número")
    if len(l) == 0:
        print("No has introducido números así que la lista está vacía")
    else:
        print(f"El primer índice en que que la suma de las mitades es igual es {busca_indice(l)}")
# end main