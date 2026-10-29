# Solución de Ecuaciones Diferenciales: Analítica vs. Numérica

Este proyecto aborda la resolución de una **ecuación diferencial ordinaria (EDO) de primer orden separable**, comparando la solución analítica exacta (obtenida mediante el método de **Separación de Variables**) con una solución aproximada calculada mediante el **Método de Euler**.

---

## Planteamiento del Problema

Dada la ecuación diferencial separable:

$$\frac{dy}{dt} = -2ty$$

Con la condición inicial:

$$y(0) = 1$$

Se requiere evaluar el comportamiento de $y(t)$ en el intervalo $t \in [0, 1]$ utilizando un tamaño de paso $h = 0.2$.

---

## 1. Solución Analítica (Separación de Variables)

### Paso 1: Separación de términos
Agrupamos todas las variables $y$ de un lado de la igualdad y $t$ del otro:

$$\frac{1}{y} \, dy = -2t \, dt$$

### Paso 2: Integración a ambos lados
$$\int \frac{1}{y} \, dy = \int -2t \, dt$$

$$\ln|y| = -t^2 + C_1$$

### Paso 3: Despeje de $y(t)$
Aplicando la función exponencial en ambos miembros:

$$|y| = e^{-t^2 + C_1} = e^{C_1} \cdot e^{-t^2}$$

Definiendo $C = e^{C_1}$:

$$y(t) = C \cdot e^{-t^2}$$

### Paso 4: Aplicación de la Condición Inicial
Dado que $y(0) = 1$:

$$1 = C \cdot e^{0} \implies C = 1$$

### **Solución Exacta:**
$$y(t) = e^{-t^2}$$

---

## 2. Método Numérico (Euler)

El esquema iterativo del método de Euler para este problema es:

$$y_{n+1} = y_n + h \cdot f(t_n, y_n)$$

Donde $f(t, y) = -2ty$ y $h = 0.2$.

### Iteraciones ($t \in [0, 1]$)

* **$t_0 = 0.0$:** $y_0 = 1.0$
* **$t_1 = 0.2$:** $y_1 = 1.0 + 0.2(-2 \cdot 0 \cdot 1) = 1.0$
* **$t_2 = 0.4$:** $y_2 = 1.0 + 0.2(-2 \cdot 0.2 \cdot 1.0) = 0.96$
* **$t_3 = 0.6$:** $y_3 = 0.96 + 0.2(-2 \cdot 0.4 \cdot 0.96) = 0.8064$
* **$t_4 = 0.8$:** $y_4 = 0.8064 + 0.2(-2 \cdot 0.6 \cdot 0.8064) = 0.612864$
* **$t_5 = 1.0$:** $y_5 = 0.612864 + 0.2(-2 \cdot 0.8 \cdot 0.612864) = 0.416748$

---

## Comparación de Resultados

| $t$ | Euler (Aproximación) | Exacta ($e^{-t^2}$) | Error Absoluto |
|:---:|:--------------------:|:-------------------:|:--------------:|
| 0.0 | 1.000000 | 1.000000 | 0.000000 |
| 0.2 | 1.000000 | 0.960789 | 0.039211 |
| 0.4 | 0.960000 | 0.852144 | 0.107856 |
| 0.6 | 0.806400 | 0.697676 | 0.108724 |
| 0.8 | 0.612864 | 0.527292 | 0.085572 |
| 1.0 | 0.416748 | 0.367879 | 0.048868 |

---

## Ejecución del Código

Para ejecutar la simulación en Python:

```bash
python separacion_variables_euler.py
