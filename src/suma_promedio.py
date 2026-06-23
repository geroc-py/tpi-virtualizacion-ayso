# UTN\Arquitectura y Sistemas Operativos\Trabajo Práctico Integrador
# Alumno: Cardoso, Gerónimo José
# Comisión: M2026-13

# Programa que solicita 5 enteros positivos al usuario, los suma y promedia y muestra ambos resultados en pantalla.
# -----------------------------------------------------------------------------------------------------------------

cantidad_numeros = 5


# Definición de funciones 

# Función para solicitar y validar el ingreso de enteros positivos
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("ERROR. Ingrese un número entero (ValueError).")
            continue

        if valor <= 0:
            print("ERROR. Ingrese un número positivo (ValueError).")
            continue

        return valor

# Función para crear una lista con todos los números ingresados
def lista_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        numero = pedir_entero(f"Ingrese el entero positivo N° {i+1}: ")
        numeros.append(numero)

    return numeros

# Función para sumar los números ingresados
def sumar_numeros(numeros):
    return sum(numeros)

# Función para promediar los números ingresados
def promediar_numeros(numeros):
    return sumar_numeros(numeros) / len(numeros)


# Función del programa principal
def main():
    print("   Programa Simple de Sumas y Promedios   \n")

    numeros = lista_numeros(cantidad_numeros)
    suma = sumar_numeros(numeros)
    promedio = promediar_numeros(numeros)

    print(f"\nNúmeros ingresados: {numeros}")
    print(f"La suma de los {cantidad_numeros} números es: {suma}")
    print(f"El promedio es: {promedio:.2f}")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
