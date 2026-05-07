# 📘 README - Algoritmos de Exponenciación y Criptografía Clásica

## 📌 Descripción general

Este proyecto contiene una colección de ejercicios en Python enfocados en:

- Representación binaria de exponentes
- Exponenciación eficiente (Cuadrado y Multiplicación)
- Análisis de complejidad computacional
- Exponenciación modular
- Cifrados clásicos: César y Afín

Cada ejercicio aborda un concepto específico y construye sobre el anterior.

---

## 🧩 Ejercicio 1: Exponente a Binario

### 🔹 Objetivo
Convertir un exponente decimal a su representación binaria.

### 🔹 Funcionamiento

- Se usa recursividad para dividir el exponente entre 2.
- Se almacenan los residuos (bits).
- El resultado es una lista de bits.

```python
exponente_a_binario(base, exponente)
```

### 🔹 Concepto clave

$$
n = \sum b_i \cdot 2^i
$$

---

## 🧩 Ejercicio 2: Cuadrado y Multiplicación

### 🔹 Objetivo
Calcular $base^{exponente}$ de forma eficiente usando la representación binaria.

### 🔹 Funcionamiento

- Se recorre el exponente en binario.
- Por cada bit:
  - Se eleva al cuadrado el acumulador.
  - Si el bit es 1, se multiplica por la base.

### 🔹 Algoritmo

1. Inicializar acumulador en 1
2. Para cada bit:
   - Cuadrar acumulador
   - Si bit = 1 → multiplicar por base

### 🔹 Ventaja

Reduce complejidad de:

- Ingenuo: $O(n)$
- Eficiente: $O(\log n)$

---

## 🧩 Ejercicio 3: Conteo de Operaciones

### 🔹 Objetivo
Comparar el número de operaciones entre:

- Método ingenuo
- Algoritmo AER (Cuadrado y Multiplicación)

### 🔹 Métodos

#### Ingenuo

$$
base^n = base \cdot base \cdot ... \cdot base
$$

→ n multiplicaciones

#### AER

- 1 operación por bit (cuadrado)
- +1 si el bit es 1

### 🔹 Resultado

Se imprime un gráfico en texto mostrando el ahorro:

```
Ingenuo: 0000000000
AER:     0000
```

---

## 🧩 Ejercicio 4: Exponenciación Modular

### 🔹 Objetivo
Calcular:

$$
base^{exponente} \mod m
$$

### 🔹 Funcionamiento

- Aplica Cuadrado y Multiplicación
- Reduce módulo en cada paso

```python
(acumulador ** 2) % modulo
```

### 🔹 Ventaja

- Evita overflow
- Fundamental en criptografía (ej: RSA)

---

## 🧩 Ejercicio 5: Cifrado César

### 🔹 Objetivo
Implementar cifrado por desplazamiento en alfabeto español.

### 🔹 Fórmula

$$
C_i = (M_i + k) \mod 27
$$

- $M_i$: posición de la letra
- $k$: desplazamiento

### 🔹 Funcionalidades

- Cifrado de texto
- Ataque por fuerza bruta
- Evaluación con diccionario

### 🔹 Flujo

1. Cifrar texto
2. Probar todos los desplazamientos
3. Elegir el mejor resultado según coincidencias

---

## 🧩 Ejercicio 6: Cifrado Afín

### 🔹 Objetivo
Generalizar el cifrado César usando una función lineal.

### 🔹 Fórmula

$$
C_i = (a \cdot M_i + b) \mod 27
$$

### 🔹 Restricción

$$
\gcd(a, 27) = 1
$$

→ garantiza inversa modular

### 🔹 Funcionamiento

- Verifica si $a$ es primo relativo con 27
- Aplica transformación letra por letra

---

## 🔗 Relación entre ejercicios

```
Binario → Exponenciación eficiente → Optimización → Modular → Criptografía
```

---

## ⚙️ Ejecución

Cada ejercicio tiene su propio `menu()`:

```bash
python ejercicio_X.py
```

---

## 📚 Conceptos clave

- Recursividad
- Representación binaria
- Complejidad algorítmica
- Aritmética modular
- Criptografía clásica

---

---

# 🧪 Archivo de pruebas integradas: `prueba.py`

## 📌 Propósito

El archivo `prueba.py` permite ejecutar todos los ejercicios del proyecto desde un único menú interactivo.

Sirve para:

- Verificar el funcionamiento de cada módulo
- Probar la integración entre ejercicios
- Comparar algoritmos
- Ejecutar demostraciones rápidas
- Validar resultados sin abrir cada archivo individualmente

---

## 📂 Estructura esperada del proyecto

```text
proyecto/
│
├── ejercicio_1.py
├── ejercicio_2.py
├── ejercicio_3.py
├── ejercicio_4.py
├── ejercicio_5.py
├── ejercicio_6.py
│
├── prueba.py
└── README.md
```

---

## ▶️ Cómo ejecutar

Ubicarse en la carpeta del proyecto y ejecutar:

```bash
python prueba.py
```

o en algunos sistemas:

```bash
python3 prueba.py
```

---

## 🖥️ Menú principal

Al ejecutar el archivo aparecerá un menú similar a:

```text
PROYECTO DE EXPONENCIACIÓN Y CRIPTOGRAFÍA

1. Probar Ejercicio 1
2. Probar Ejercicio 2
3. Probar Ejercicio 3
4. Probar Ejercicio 4
5. Probar Ejercicio 5
6. Probar Ejercicio 6
7. Ejecutar TODO
0. Salir
```

---

## 🔍 Qué realiza cada opción

| Opción | Función |
|---|---|
| 1 | Conversión de exponentes a binario |
| 2 | Exponenciación eficiente |
| 3 | Comparación de operaciones |
| 4 | Exponenciación modular |
| 5 | Cifrado César y fuerza bruta |
| 6 | Cifrado Afín |
| 7 | Ejecuta todas las pruebas |
| 0 | Finaliza el programa |

---

## 📌 Requisitos

- Python 3.x
- Archivos del proyecto en la misma carpeta
- Consola o terminal

Verificar versión:

```bash
python --version
```

---

## ⚠️ Posibles errores comunes

### Error: `ModuleNotFoundError`

Ocurre cuando un archivo no se encuentra en la carpeta.

Verificar:

```text
ejercicio_1.py
ejercicio_2.py
...
```

---

### Error de recursividad

El ejercicio 4 aumenta el límite con:

```python
sys.setrecursionlimit(5000)
```

Si se usan exponentes muy grandes puede ser necesario aumentar ese valor.

---

## 🧠 Objetivo académico del archivo de pruebas

Este archivo permite estudiar:

- Modularización
- Reutilización de funciones
- Importación entre archivos
- Integración de algoritmos
- Automatización de pruebas básicas

---