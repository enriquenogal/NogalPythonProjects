# cabecera de la clase con su nombre, también se puede poner class Persona(object): lo cual define que hereda de la clase object
class Persona:
    # en realidad no hay porque definir los atributos si ya están definidos en el constructor
    # te puede servir la definición para definir algún atributo extra que no esté en el constructor como es en este caso la energía que se inicializa a 0.0
    codigo = ""
    nombre = ""
    apellido = ""
    energia = 0.0
    # esto me puede servir como una definición de un atributo estático
    # en realidad es un atributo que se podría usar en cada objeto de modo que sería de cada instancia pero no de la clase
    # el modo de convertirlo en estático es en la llamada a este atributo (mira la última línea del contructor)
    # ver código del ejecutable para ver cómo se le llama desde fuera
    contador = 0 
    # no existen atributos protegidos o privados en Python, aunque los programadores llegan a un convenio de modo que se nombran de un modo especial
    # _salario vendría a ser protegido. Sólo debería ser usado desde esta clase y sus subclases
    # __salario vendría a ser privado. Sólo debería ser usado desde esta misma clase
    # Si un atributo comienza con dos guiones bajos ( __atributo ), Python realiza una manipulación de nombres (name mangling). 
    # Esto cambia el nombre del atributo internamente para evitar conflictos con nombres de atributos en subclases. 
    # Por ejemplo, __atributo se convertiría en _NombreClase__atributo.
    __salario = 0.0

    # no se pueden definir varios constructores
    # pero se puede simular pasando como parámetro al constructor una tupla, lista o diccionario y poniendo unos if para ver qué datos cargar
    def __init__(self, codigo, nombre, apellido):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        Persona.contador += 1
    
    # si no se define este método hacer print va a funcionar pero no mostrará la información sino que otra cosa que no da información real
    def __str__(self): 
        """
        Purpose: 
        """
        return self.codigo + ":" + self.nombre + ":" + self.apellido + ":" + str(self.energia) + ":" + str(self.__salario)
    
    # no existe la sobrecarga de modo que no se pueden tener dos métodos "comer" en la misma clase
    # se pueden hacer otras cosas como pasar un dicionario y montar unos if tal y como vemos en el ejemplo
    def comer(self,data):
        if "comida" in data:
            self.energia += data["comida"] / 2
        else:
            self.energia += 5

    # método estático
    # la diferencia es que no se le pasa el parámetro self y en la llamada (ver código del ejecutable)
    def cuantos():
        return Persona.contador
    
    # ejemplo de una función en la que tendría sentido el atributo privado 
    # que sólo debería ser manejado desde esta función de modo que el salario no pudiera estar fuera de unos límites
    def subir_salario(self,subida):
        self.__salario += subida
        if self.__salario < 0 or self.__salario > 100000:
            self.__salario -= subida
            return False
        else:
            return True
        
    # hay funciones especiales que podrían servir por ejemplo para comparar objetos como esta de __lt__ que sirve para comparaciones <
    # hay otras que puedes implementar
    # __add__ corresponde con +
    # __eq__ corresponde con ==
    # __sub__ corresponde con -   
    def __lt__(self,other):
        if self.__salario < other.__salario:
            return True
        else:
            return False

    
