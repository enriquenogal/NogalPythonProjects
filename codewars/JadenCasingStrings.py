# Jaden Casing Strings


def to_jaden_case(string):
    l = string.split(" ")
    salida = ""
    for p in l:
        salida = salida + p.capitalize() + " "
    return salida.strip()
    # ...


if __name__ == "__main__":
    print(to_jaden_case("hola que tal"))
# end main

