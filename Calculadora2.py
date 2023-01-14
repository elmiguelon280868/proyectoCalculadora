import math

# Esta funcion se ocupa para Sumar dos numeros
def sumar(P, Q):
    return P + Q

# Esta funcion se ocupa para restar dos numeros
def restar(P, Q):
    return P - Q

# Esta funcion se ocupa para multiplicar dos numeros
def multiplicar(P, Q):
    return P * Q

# Esta funcion se ocupa para dividir dos numeros
def dividir(P, Q):
    return P / Q

# Se toman lo numeros ingresados por el usuario
choice = 0
while True:
    print(""""
    ¿Que operacion quieres realizar?
    
    1) Sumar dos números
    2) Restar dos números
    3) Multiplicar dos números
    4) Dividir dos números
    5) Raiz de un número
    6) Exponente de un número
    7) Función Seno
    8) Apagar la calculadora
    """)
    choice = int(input("Por favor elige una opción: "))

    # suma
    if choice == 1:
        num_1 = int(input("Por favor ingrese el primer numero: "))
        num_2 = int(input("Por favor ingrese el segundo numero: "))
        print(num_1, " + ", num_2, " = ", sumar(num_1, num_2))

    # resta
    elif choice == 2:
        num_1 = int(input("Por favor ingrese el primer numero: "))
        num_2 = int(input("Por favor ingrese el segundo numero: "))
        print(num_1, " - ", num_2, " = ", restar(num_1, num_2))

    # mutiplicación
    elif choice == 3:
        num_1 = int(input("Por favor ingrese el primer numero: "))
        num_2 = int(input("Por favor ingrese el segundo numero: "))
        print(num_1, " * ", num_2, " = ", multiplicar(num_1, num_2))

    # dividir
    elif choice == 4:
        num_1 = int(input("Por favor ingrese el primer numero: "))
        num_2 = int(input("Por favor ingrese el segundo numero: "))
        print(num_1, " / ", num_2, " = ", dividir(num_1, num_2))

    # raiz
    elif choice == 5:
        num_1 = int(input("Por favor ingrese el numero a calcular : "))
        y = math.sqrt(num_1)
        print("La raiz es:", y)

    # exponencial
    elif choice == 6:
        num_1 = int(input("Por favor ingrese el numero base : "))
        num_2 = int(input("Por favor ingrese el numero de exponencial : "))
        y = num_1 ** num_2
        print("El resultado es:", y)

    # seno
    elif choice == 7:
        num_1 = int(input("Por favor ingrese el número  : "))
        y = math.radians(num_1)
        x = math.sin(y)
        print("El resultado es:", x)

    elif choice == 8:
        break

    else:
        print("Opción no existe ingrese una opción valida")
