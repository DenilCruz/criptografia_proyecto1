from primer_ejercicio import exponente_a_binario


def contar_operaciones_ingenuo(base, exponente):
    if exponente == 0:
        return  0
    else:
        return 1 + contar_operaciones_ingenuo(base, exponente - 1)

def contar_aer(base, exponente):
    lista_de_bits = list(exponente_a_binario(base,exponente)) 
    operaciones_totales = resultado_final(base, lista_de_bits, contador=0)
    return operaciones_totales

    
def resultado_final(base, lista_de_bits_del_exponente, contador):
    if not lista_de_bits_del_exponente:
        return contador
    
    bit_actual = lista_de_bits_del_exponente.pop(0)
    contador += 1
    
    if bit_actual == 1:
        contador += 1
        
    return resultado_final(base, lista_de_bits_del_exponente, contador)

def menu():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    resultado = contar_operaciones_ingenuo(base, exponente)
    print(f"\nel número de operaciones es: {resultado}")

def grafico_terminal_comparacion():
    base = 2
    exponentes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50] 
    
    print("\n" + "="*70)
    print(" ANÁLISIS DE AHORRO DE CÓMPUTO: INGENUO VS AER")
    print(" (Cada '0' representa 1 operación)")
    print("="*70 + "\n")
    
    for e in exponentes:
        ops_i = contar_operaciones_ingenuo(base, e)
        ops_a = contar_aer(base, e)
        
        # Calcular el porcentaje de ahorro
        ahorro = (1 - (ops_a / ops_i)) * 100 if ops_i > 0 else 0
        
        # Crear las "barras" de texto
        barra_ingenuo = "0" * ops_i
        barra_aer = "0" * ops_a
        
        # Destacar visualmente si superamos el 80%
        if ahorro > 80:
            alerta = " <<< ¡BARRERA DEL 80% SUPERADA! >>>"
        else:
            alerta = ""
            
        # Imprimir el bloque para este exponente
        print(f"Exponente: {e} | Ahorro: {ahorro:.1f}% {alerta}")
        print(f"Ingenuo ({ops_i}): {barra_ingenuo}")
        print(f"AER     ({ops_a}): {barra_aer}")
        print("-" * 70)


if __name__ == "__main__":
    grafico_terminal_comparacion()
    #menu()