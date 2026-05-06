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