def equilibrado(str):
    pila = []
    for c in str:
        if c in ('[','(','{'): pila.append(c)
        if c == ']': 
            if pila[-1] == '[': pila.pop()
            else: return False
        if c == ')': 
            if pila[-1] == '(': pila.pop()
            else: return False
        if c == '}': 
            if pila[-1] == '{': pila.pop()
            else: return False
    if len(pila) == 0: return True
    return False

if __name__ == "__main__":
    str = ""
    while str.upper() != "FIN":
        str = input("Dame una cadena de texto: ")
        if str.upper() != "FIN":
            if equilibrado(str):
                print("SI está correctamente balanceada")
            else:
                print("NO está correctamente balanceada")
# end main