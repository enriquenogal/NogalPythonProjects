
if __name__ == "__main__":
    x = int(input("Ancho del cuboide: "))
    y = int(input("Alto del cuboide: "))
    z = int(input("Fondo del cuboide: "))
    condicion = int(input("Número condición: "))
    # Estas serían todas las permutaciones
    permutaciones = [(i,j,k) for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1)]
    print(permutaciones)

    permutacionesCondicion =\
    [(i,j,k) for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != 1]

    print("Condición:",permutacionesCondicion)

    permutacionesSuelo = \
    [(i,j,k) for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if k == 0]

    print("Suelo:",permutacionesSuelo)

    permutacionesTecho = \
    [(i,j,k) for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if k == z]

    print("Techo:",permutacionesTecho)

    permutacionesParedDerecha = \
    [(i,j,k) for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i == x]

    print("Pared derecha:",permutacionesParedDerecha)
# end main