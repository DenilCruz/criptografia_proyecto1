letra = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def primo_relativo(a,b):
    if a == 0 or b == 0:
        return False
    if a == 1 or b == 1:
        return True
    if a == b:
        return False
    if a > b:
        return primo_relativo(a - b, b)
    else:
        return primo_relativo(a, b - a)
    
def cifrado_afin(texto, desplazamiento, multiplicador):
    texto_mayusculas = texto.upper()
    if primo_relativo(multiplicador, 27):
        return cifrado_letra_por_letra(texto_mayusculas, desplazamiento, multiplicador, resultado="", indice=0)
    else:
        raise ValueError("El multiplicador y el desplazamiento deben ser primos relativos.")
    
def cifrado_letra_por_letra(texto, desplazamiento, multiplicador, resultado, indice):
    if indice == len(texto):
        return resultado
    
    letra_actual = texto[indice]
    if letra_actual in letra:
        posicion = letra.index(letra_actual)
        nueva_posicion = (multiplicador * posicion + desplazamiento) % 27
        resultado += letra[nueva_posicion]
    else:
        resultado += letra_actual

    return cifrado_letra_por_letra(texto, desplazamiento, multiplicador, resultado, indice + 1)


def menu():
    texto = input("Ingrese el texto a cifrar: ")
    desplazamiento = int(input("Ingrese el desplazamiento: "))
    multiplicador = int(input("Ingrese el multiplicador: "))
    
    try:
        texto_cifrado = cifrado_afin(texto, desplazamiento, multiplicador)
        print(f"\nTexto cifrado: {texto_cifrado}")
    except ValueError as e:
        print(e)   

if __name__ == "__main__":
    menu()