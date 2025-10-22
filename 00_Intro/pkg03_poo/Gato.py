from Animal import Animal

class Gato(Animal):

    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def comer(self):
        self.set_energia(self.get_energia() + 10)
