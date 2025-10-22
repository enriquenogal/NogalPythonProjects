from Persona import Persona

class Alumno(Persona):

    titulacion = ""
    curso = 0

    def __init__(self, codigo, nombre, apellido, energia, titulacion, curso):
        super().__init__(codigo, nombre, apellido)
        self.energia = energia
        self.titulacion = titulacion
        self.curso = curso

    def __str__(self):
        return super().__str__() + ":" + self.titulacion + ":" + str(self.curso)

    def comer(self,data):
        self.energia += 150