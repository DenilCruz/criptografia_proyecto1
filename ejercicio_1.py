def exponente_a_binario(base, exponente):
    if exponente == 0:
        return []
    lista = exponente_a_binario(base, exponente // 2)
    residuo = exponente % 2
    lista.append(residuo)
    return lista

def calcular_pesos(lista_bits):
    n = len(lista_bits)
    pesos = [2**(n-1-i) for i in range(n)]
    return pesos

def mostrar_horizontal(bits, secuencia):
    print("   ".join(map(str, secuencia)))
    print("   ".join(map(str, bits)))



def menu():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    resultado = exponente_a_binario(base, exponente)
    print(f"El resultado de {base} elevado a {exponente} en binario es: {resultado}")
    secuencia = calcular_pesos(resultado)
    mostrar_horizontal(resultado, secuencia)

if __name__ == "__main__":
    menu()
