import os

if __name__ == "__main__":
    # veamos si existe
    if os.path.exists("demofile.txt"):
        print("demofile.txt existe")
    else:
        print("demofile.txt no existe")
    linea = ""
    # usando with ya no tendrás que hacer el cierre del fichero
    with open("demofile.txt", "a") as f: # esto hace un append si existe
    # with open("demofile.txt", "w") as f: # esto sobreescribe el fichero si existe
        while linea != "*": 
            linea = input("Introduce una línea (* para terminar): ")  
            if linea != "*": 
                f.write(linea + "\n")
# end main