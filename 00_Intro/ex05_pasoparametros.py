# los parámetros llegan al programa a través de la tupla sys.argv
# si no se envían parámetros hay un parámetro vacío en sys.argv
# pero cuando si que se le envían parámetros el primer parámetro que se recibe es el nombre del ejecutable

import sys # hay que importar sys para poder recurrir a los parámetros

if __name__ == "__main__":
    print("Paso de parámetros")
    print("Número de parámetros:",len(sys.argv)) 
    if len(sys.argv) != 1:
        for parametro in sys.argv:
            print(parametro)
    else:
        print("Sin parámetros")

# end main