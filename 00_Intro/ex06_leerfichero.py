
if __name__ == "__main__":
    # f = open("demofile.txt", "rt") # así lo abres en modo lectura "r" y es de texto "t"
    # f = open("demofile.txt") es lo mismo que lo anterior, pues por defecto se abren "rt"
    # f.close() si lo abres como anteriormente se tiene que cerrar con este close

    # mucho mejor abrirlo con with ya que así python se ocupa de cerrarlo

    with open("demofile.txt") as f:
        # v = f.read(5) # así se leen los 5 primeros caracteres
        # linea = f.readline() # así se lee una línea
        # completo = f.read() # así se lee el fichero completo
        i = 1
        for x in f: # así se lee línea a línea
            print("linea",i,":",x)
            i += 1

# end main


