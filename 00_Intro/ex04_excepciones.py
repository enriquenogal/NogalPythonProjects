import traceback

def checkerNumber(str):
    if not(str.isdigit()):
        # raise Exception("Genero excepción. Número incorrecto")
        raise ValueError("Genero excepción. Número incorrecto")
    return True

def division(one, two):
    assert not two == 0, "división por cero" # si la condición no se cumple AssertionError es raised
    return one / two
# end def

if __name__ == "__main__":
    print("Excepciones")
    b = False
    while b == False:
        try:
            val1 = int(input("Dame un número: "))
            val2 = int(input("Dame un número: "))
            val3 = val1 / val2
            b = True
        except ValueError:
            print("Formato de número incorrecto")
        except Exception as e: # se puede poner simplemente except: pero si quieres mostrar algo de info la tienes que poner de este modo
            print(f"Ha ocurrido un error. Detalles: {e}")
            # traceback.print_exc() # esto te va a dar más detalles de dónde se ha producido el error. Hay que hacer un import
        else: # este se ejecuta si no ha saltado ninguna excepción
            print("Resultado:",val3)
        finally:
            print("Esto se ejecuta siempre")

    val4 = input("Dame un número: ")
    try:
        checkerNumber(val4)
    except Exception as e:
        print(f"Error: {e}")
    except:
        print("Aquí no va a llegar porque Exception ya se come todo")

    try:
        division(4,0)
    except AssertionError as e:
        print(f"Error: {e}")
# end main