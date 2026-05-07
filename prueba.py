from ejercicio_1 import exponente_a_binario, calcular_pesos
from ejercicio_2 import cuadrado_y_multiplicacion
from ejercicio_3 import (
    contar_operaciones_ingenuo,
    contar_aer,
    grafico_terminal_comparacion
)
from ejercicio_4 import calcular_tiempo
from ejercicio_5 import (
    cifrado_cesar,
    fuerza_bruta_cesar,
    evaluar_resultados,
    diccionario_español
)
from ejercicio_6 import cifrado_afin


def separador():
    print("\n" + "=" * 60 + "\n")


# =========================================================
# PRUEBA EJERCICIO 1
# =========================================================
def probar_ejercicio_1():
    separador()
    print("EJERCICIO 1 - EXPONENTE A BINARIO")

    base = 2
    exponente = 13

    bits = exponente_a_binario(base, exponente)
    pesos = calcular_pesos(bits)

    print(f"Base: {base}")
    print(f"Exponente: {exponente}")
    print(f"Binario: {bits}")
    print(f"Pesos:   {pesos}")


# =========================================================
# PRUEBA EJERCICIO 2
# =========================================================
def probar_ejercicio_2():
    separador()
    print("EJERCICIO 2 - CUADRADO Y MULTIPLICACIÓN")

    base = 2
    exponente = 13

    resultado = cuadrado_y_multiplicacion(base, exponente)

    print(f"\nResultado final: {base}^{exponente} = {resultado}")


# =========================================================
# PRUEBA EJERCICIO 3
# =========================================================
def probar_ejercicio_3():
    separador()
    print("EJERCICIO 3 - ANÁLISIS DE OPERACIONES")

    base = 2
    exponente = 50

    ingenuo = contar_operaciones_ingenuo(base, exponente)
    aer = contar_aer(base, exponente)

    print(f"Operaciones ingenuas: {ingenuo}")
    print(f"Operaciones AER:      {aer}")

    grafico_terminal_comparacion()


# =========================================================
# PRUEBA EJERCICIO 4
# =========================================================
def probar_ejercicio_4():
    separador()
    print("EJERCICIO 4 - EXPONENCIACIÓN MODULAR")

    base = 7
    exponente = 128
    modulo = 13

    tiempo = calcular_tiempo(base, exponente, modulo)

    print(f"Base: {base}")
    print(f"Exponente: {exponente}")
    print(f"Módulo: {modulo}")
    print(f"Tiempo de ejecución: {tiempo:.8f} segundos")


# =========================================================
# PRUEBA EJERCICIO 5
# =========================================================
def probar_ejercicio_5():
    separador()
    print("EJERCICIO 5 - CIFRADO CÉSAR")

    texto = "Don Quijote y Sancho Panza"
    desplazamiento = 3

    cifrado = cifrado_cesar(texto, desplazamiento)

    print(f"Texto original : {texto}")
    print(f"Texto cifrado  : {cifrado}")

    resultados = fuerza_bruta_cesar(cifrado)

    mejor_indice, coincidencias, texto_ganador = evaluar_resultados(
        diccionario_español,
        resultados
    )

    print("\nMejor resultado encontrado:")
    print(f"Desplazamiento: {mejor_indice}")
    print(f"Coincidencias : {coincidencias}")
    print(f"Texto         : {texto_ganador}")


# =========================================================
# PRUEBA EJERCICIO 6
# =========================================================
def probar_ejercicio_6():
    separador()
    print("EJERCICIO 6 - CIFRADO AFÍN")

    texto = "Caballero Andante"
    desplazamiento = 5
    multiplicador = 2

    try:
        cifrado = cifrado_afin(
            texto,
            desplazamiento,
            multiplicador
        )

        print(f"Texto original: {texto}")
        print(f"Texto cifrado : {cifrado}")

    except ValueError as e:
        print(f"Error: {e}")


# =========================================================
# MENÚ GENERAL
# =========================================================
def menu_general():

    while True:

        separador()

        print("PROYECTO DE EXPONENCIACIÓN Y CRIPTOGRAFÍA")
        print("1. Probar Ejercicio 1")
        print("2. Probar Ejercicio 2")
        print("3. Probar Ejercicio 3")
        print("4. Probar Ejercicio 4")
        print("5. Probar Ejercicio 5")
        print("6. Probar Ejercicio 6")
        print("7. Ejecutar TODO")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            probar_ejercicio_1()

        elif opcion == "2":
            probar_ejercicio_2()

        elif opcion == "3":
            probar_ejercicio_3()

        elif opcion == "4":
            probar_ejercicio_4()

        elif opcion == "5":
            probar_ejercicio_5()

        elif opcion == "6":
            probar_ejercicio_6()

        elif opcion == "7":
            probar_ejercicio_1()
            probar_ejercicio_2()
            probar_ejercicio_3()
            probar_ejercicio_4()
            probar_ejercicio_5()
            probar_ejercicio_6()

        elif opcion == "0":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción inválida.")


# =========================================================
# MAIN
# =========================================================
if __name__ == "__main__":
    menu_general()