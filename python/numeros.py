print("========BIENVENIDO A MI CALCULADORA =========")
from math import sqrt

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def potencia(base, exp):
    return base ** exp

def raiz_cuadrada(n):
    if n < 0:
        return "Error: no se puede sacar raíz de un número negativo"
    return sqrt(n)

while True:
    print("\n--- Calculadora ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '0':
        print("¡Hasta luego!")
        break

    if opcion == '6':  # Raíz solo necesita un número
        n = float(input("Ingresa el número: "))
        print(f"Resultado: {raiz_cuadrada(n)}")
    elif opcion in ('1','2','3','4','5'):
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        if opcion == '1':
            print(f"Resultado: {suma(a, b)}")
        elif opcion == '2':
            print(f"Resultado: {resta(a, b)}")
        elif opcion == '3':
            print(f"Resultado: {multiplicacion(a, b)}")
        elif opcion == '4':
            print(f"Resultado: {division(a, b)}")
        elif opcion == '5':
            print(f"Resultado: {potencia(a, b)}")
    else:
        print("Opción inválida")