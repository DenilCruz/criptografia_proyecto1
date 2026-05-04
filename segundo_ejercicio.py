# Asumo que en 'primer_ejercicio.py' la función devuelve una lista o string de bits
from primer_ejercicio import exponente_a_binario

def cuadrado_y_multiplicacion(base, exponente):
    lista_de_bits = list(exponente_a_binario(base,exponente)) 
    resultado = resultado_final(base, lista_de_bits, acumulador=1)
    return resultado

    
def resultado_final(base, lista_de_bits_del_exponente, acumulador):
    if not lista_de_bits_del_exponente:
        return acumulador

    bit_actual = str(lista_de_bits_del_exponente.pop(0))
    acumulador = acumulador ** 2
    print(f"Bit {bit_actual} -> CUADRADO: El acumulado ahora es {acumulador}")
    
    if bit_actual == '1':
        acumulador = acumulador * base
        print(f"Bit {bit_actual} -> MULTIPLICACIÓN: El acumulado ahora es {acumulador}")
    else:
        print(f"Bit {bit_actual} -> (No hay multiplicación)")

    print("-" * 20)

    return resultado_final(base, lista_de_bits_del_exponente, acumulador)


def menu():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    resultado = cuadrado_y_multiplicacion(base, exponente)
    print(f"\n¡Cálculo terminado! El resultado de {base} elevado a {exponente} es: {resultado}")


if __name__ == "__main__":
    menu()