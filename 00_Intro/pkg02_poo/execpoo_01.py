from Persona import Persona

if __name__ == "__main__":
    p1 = Persona("a000","Juan","Lopez")
    p2 = Persona("a001","Pepe","Pérez")
    # python te permite crear atributos de un objeto desde fuera de esa clase
    # es horrible y se considera una mala práctica hacerlo pero es un ejemplo de cosa que permite python
    p1.apodo = "El Potingas"
    print("----------------------------------------")
    print(p1)
    print(p2)
    print("Contador:",Persona.contador)
    print("Contador:",Persona.cuantos())
    p1.comer({})
    p2.comer({"comida":25})
    print("----------------------------------------")
    print(p1)
    print(p2)
    p1.subir_salario(1000)
    p2.subir_salario(-1)
    print("----------------------------------------")
    print(p1)
    print(p2)
    # Aquí vemos lo del Name mangling. Además podemos apreciar que aunque sea privado se puede seguir accediendo a el atributo
    # de modo que nos damos cuenta que estas definiciones no son reales sino que son un convenio al que se ha llegado y que se puede no respetar
    p2._Persona__salario += -1 
    print("----------------------------------------")
    print(p1)
    print(p2)
    print("----------------------------------------")
    # en realidad estamos llamando a la funcion __lt__
    if p1 < p2:
        print("Juan tiene menor salario que Pepe")
    else:
        print("Pepe tiene menor o igual salario que Juan")

# end main