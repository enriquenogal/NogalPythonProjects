from Animal import Animal
from Perro import Perro
from Gato import Gato

if __name__ == "__main__":
    # a = Animal("pepe") # esta línea no va a funcionar
    p = Perro("juan","doberman")
    g = Gato("antonio","naranja")
    l = [p,g]
    for item in l:
        item.comer()
        print(item)
# end main