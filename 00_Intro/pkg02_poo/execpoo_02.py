from Persona import Persona
from Profesor import Profesor
from Alumno import Alumno

if __name__ == "__main__":
    prof1 = Profesor("pr01","Juan","Lopez",100,"informática")
    alum1 = Alumno("al01","Tomas","Narros",0,"DAM",1)
    print("--------------------------------------")
    print(prof1)
    print(alum1)
    prof1.comer({})
    alum1.comer({})
    print("--------------------------------------")
    print(prof1)
    print(alum1)
    print("--------------------------------------")
    lista = [prof1,alum1]
    for item in lista:
        if isinstance(item,Profesor):
            print("Profesor:",item)
        elif isinstance(item,Alumno):
            print("Alumno:",item)
    print("--------------------------------------")
    print(type(prof1))
    print(type(alum1))

# end main