a1 = int(input('Ingrese el primer número: '))
a2 = int(input('Ingrese el segundo número: '))

def sucesor(n):
    return n + 1

def antecesor(n):
    if n > 0:
        return n - 1
    else:
        return "No se puede calcular el antecesor de 0"

def suma(a, b):
    while b != 0:
        if b > 0:
            a = sucesor(a)
            b = antecesor(b)
    return a

def resta(a, b):
    while b != 0:
        if a == 0:
           return "No se puede calcular la resta de 0 o inferior"
        if b > 0:
            a = antecesor(a)
            b = antecesor(b)
    return a

def multiplicacion(a, b):
    result = 0
    while b != 0:
        if b > 0:
            result = suma(result, a)
            b = antecesor(b)
    return result

def division(a, b):
    if b == 0:
        return "No se puede dividir por 0"
    result = 0
    while a >= b:
        if a >= b:
            a = resta(a, b)
            result = sucesor(result)
    return result

print("La suma da como resultado", suma(a1, a2))
print("La resta da como resultado",resta(a1, a2))
print("La multiplicacion da como resultado",multiplicacion(a1, a2))
print("La division da como resultado",division(a1, a2))

