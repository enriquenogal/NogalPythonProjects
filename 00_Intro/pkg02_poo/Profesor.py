from Persona import Persona

class Profesor(Persona):

    especialidad = ""

    def __init__(self, codigo, nombre, apellido, energia, especialidad):
        super().__init__(codigo, nombre, apellido)
        self.energia = energia
        self.especialidad = especialidad

    def __str__(self):
        return super().__str__() + ":" + self.especialidad

    def comer(self,data):
        self.energia += 50