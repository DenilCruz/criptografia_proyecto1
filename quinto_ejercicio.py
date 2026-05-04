letra = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

diccionario_español = {"DON", "QUIJOTE", "SANCHO", "PANZA", "DULCINEA", "ROCINANTE", "CABALLERO", "ANDANTE", "AVENTURA", "LANZAROTE", "GINES"}

def cifrado_cesar(texto, desplazamiento):
    texto_mayusculas = texto.upper()
    return cifrado_letra_por_letra(texto_mayusculas, desplazamiento, resultado="", indice=0)

def cifrado_letra_por_letra(texto, desplazamiento, resultado, indice):
    if indice == len(texto):
        return resultado
    
    letra_actual = texto[indice]
    
    if letra_actual in letra:
        posicion = letra.index(letra_actual)
        nueva_posicion = (posicion + desplazamiento) % 27
        resultado += letra[nueva_posicion]
    else:
        resultado += letra_actual

    return cifrado_letra_por_letra(texto, desplazamiento, resultado, indice + 1)

def fuerza_bruta_cesar(texto):
    texto_mayusculas = texto.upper()
    resultados = {} 
    
    for desplazamiento in range(27):
        texto_descifrado = fuerza_bruta_palabra_por_palabra(texto_mayusculas, "", desplazamiento, 0)
        resultados[desplazamiento] = texto_descifrado
    
    return resultados

def fuerza_bruta_palabra_por_palabra(texto, resultado, desplazamiento, indice):
    if indice == len(texto):
        return resultado
    
    letra_actual = texto[indice]
    if letra_actual in letra:
        posicion = letra.index(letra_actual)
        nueva_posicion = (posicion - desplazamiento) % 27
        resultado += letra[nueva_posicion]
    else:
        resultado += letra_actual

    return fuerza_bruta_palabra_por_palabra(texto, resultado, desplazamiento, indice + 1)

def evaluar_resultados(diccionario_espanol, diccionario_resultados):
    mejor_indice = 0
    mayor_coincidencias = 0
    texto_ganador = ""

    for indice, texto_descifrado in diccionario_resultados.items():
        
        palabras_del_texto = texto_descifrado.split()
        
        coincidencias = 0
        for palabra in palabras_del_texto:
            if palabra in diccionario_espanol:
                coincidencias += 1
        
        if coincidencias > mayor_coincidencias:
            mayor_coincidencias = coincidencias
            mejor_indice = indice
            texto_ganador = texto_descifrado

    return mejor_indice, mayor_coincidencias, texto_ganador


 
def menu():
    texto = input("Ingrese el texto a cifrar: ")
    desplazamiento = int(input("Ingrese el desplazamiento: "))
    resul = cifrado_cesar(texto, desplazamiento)
    print(f"\nEl texto cifrado es: {resul}")

    resultado = fuerza_bruta_cesar(resul)
    print(f"\nLos resultados de la fuerza bruta son:")
    for d, t in resultado.items():
        print(f"Desplazamiento {d}: {t}")

    mejor_indice, mayor_coincidencias, texto_ganador = evaluar_resultados(diccionario_español, resultado)
    print(f"\nEl mejor resultado es con desplazamiento {mejor_indice} con {mayor_coincidencias} coincidencias. El texto descifrado es: {texto_ganador}")


if __name__ == "__main__":
    menu()