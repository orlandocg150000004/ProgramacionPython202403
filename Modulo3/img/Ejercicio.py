def sumar_numeros():
    print("Por favor, ingrese dos números para sumar.")
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    suma = num1 + num2
    print("La suma de los dos números es:", suma)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calcular_sumatoria(n, p):
    if n == 1:
        return p
    else:
        return n * p + calcular_sumatoria(n - 1, p)

def menu():
    print("Bienvenido al menú interactivo")
    print("¿Qué quieres hacer? Escribe una opción")
    print("1) Sumar dos números")
    print("2) Función Factorial")
    print("3) Función K(n, p)")
    print("4) Salir")

def main():
    while True:
        menu()
        opcion = input("Opción: ")

        if opcion == '1':
            print("Hola, espero que te lo estés pasando bien")
            sumar_numeros()
        elif opcion == '2':
            numero = int(input("Ingrese un número para calcular su factorial: "))
            print("El factorial de", numero, "es:", factorial(numero))
        elif opcion == '3':
            print("¡Hasta luego! Ha sido un placer ayudarte.")
            break
        elif opcion == '4':
            opcion_factorial = input("¿Desea calcular el factorial de un número? (S/N): ")
            if opcion_factorial.lower() == 's':
                numero = int(input("Ingrese un número para calcular su factorial: "))
                print("El factorial de", numero, "es:", factorial(numero))
        elif opcion == '5':
            n = int(input("Ingrese un número n: "))
            p = int(input("Ingrese un número p: "))
            print("El resultado de K(n, p) es:", calcular_sumatoria(n, p))
        else:
            print("Comando desconocido, vuelva a intentarlo")

if __name__ == "__main__":
    main()
