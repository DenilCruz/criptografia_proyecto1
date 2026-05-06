import time
from primer_ejercicio import exponente_a_binario
import sys

sys.setrecursionlimit(5000)


def cuadrado_y_multiplicacion(base, exponente, modulo):
    lista_de_bits = list(exponente_a_binario(base, exponente)) 
    return resultado_final(base, lista_de_bits, 0, acumulador=1, modulo=modulo)

def resultado_final(base, lista_de_bits, indice, acumulador, modulo):
    if indice == len(lista_de_bits):
        return acumulador

    bit_actual = lista_de_bits[indice]

    acumulador = (acumulador ** 2) % modulo
    
    if bit_actual == 1:
        acumulador = (acumulador * base) % modulo

    return resultado_final(base, lista_de_bits, indice + 1, acumulador, modulo)

def calcular_tiempo(base, exponente, modulo):
    inicio = time.time()
    cuadrado_y_multiplicacion(base, exponente, modulo)
    fin = time.time()
    return fin - inicio

def menu ():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    modulo = int(input("Ingrese el módulo: "))
    exponente_en_binario = exponente_a_binario(base, exponente)
    tiempo = calcular_tiempo(base, exponente, modulo)   
    print(f"El exponente en binario es: {exponente_en_binario}")
    print(f"\n¡Cálculo terminado! El tiempo de ejecución fue: {tiempo:.6f} segundos")
    

if __name__ == "__main__":
    menu()
