from abc import ABC, abstractmethod

# con el import anterior y esta herencia en la cabecera de la clase defino que esta clase es abstracta
# no se podrán instanciar objetos de esta clase
class Animal(ABC):

    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 0

    def __str__(self):
        return self.nombre + ":" + str(self.energia)
    
    def get_nombre(self):
        return self.nombre
    
    # lo de poner nombre = "" se denomina default argument y sirve para todas las funciones (ya sea en POO o no)
    # esto permite no pasar ese parámetro de nombre al llamar a esta función y lo que ocurriría es que lo dejaría con el valor ""
    # esto se podría usar también para saltarse lo de que no exista sobrecarga de nombres de funciones en POO
    def set_nombre(self, nombre = ""):
        self.nombre = nombre

    def get_energia(self):
        return self.energia
    
    def set_energia(self, energia):
        self.energia = energia

    # así defino que el método es abstracto y que sus clases hijas deberán implementarlo
    @abstractmethod
    def comer(self):
        # aunque sea abracto además del método el método tiene que tener cuerpo
        # con pass se soluciona esto
        pass
        
