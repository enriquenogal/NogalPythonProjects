from Animal import Animal

class Perro(Animal):

    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def comer(self):
        self.set_energia(self.get_energia() + 20)

    