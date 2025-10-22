import random
import pkg01.ex01_lib as ex01_lib

def func1(one, two):
    """
    Purpose: one
    """
    one = 15
    return 1
# end def

if __name__ == "__main__":
    g = random.randint(4,88)
    print(g)
    str = "hola" * 3
    print(str)
    i = 4
    i *= 2
    print(i)
    #j = input("introduce un número: ")
    #j = int(j)
    #print(type(j))

    #t = type(j)
    #print(type(t))

    if 4 == 5:
        print("iguales")
        print("imposible")
    elif 4 != 5:
        print("diferentes")
    else:
        print("imposible")

    for item in range(13, 10, -1):
        print(item)
        # comment: 
    # end for


    s1 = "hola"
    for item in range(0, len(s1)):
        print(s1[item])
        # comment: 
    # end for

    for char in s1:
        print(char)
        # comment: 
    # end for

    one = 8
    print(func1(one,2))
    print(one)

    print(ex01_lib.es_par(44))

    cont = 0
    while cont < 10:
        print(cont)
        cont += 1

# end main


