
def mdc (a, b):
    if a < b:
        a, b = b, a

    resto = a % b

    while resto != 0:
        a = b
        b = resto
        resto = a % b
    return b
