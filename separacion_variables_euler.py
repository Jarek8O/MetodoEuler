"""
Solución Analítica y Numérica de una Ecuación Diferencial Separable
------------------------------------------------------------------
Ecuación: dy/dt = -2 * t * y
Condición Inicial: y(0) = 1
Intervalo: t ∈ [0, 1]
Paso: h = 0.2

1. Solución Analítica (Separación de Variables):
   dy / y = -2 * t dt
   ln|y| = -t^2 + C
   y(t) = C * e^(-t^2)
   Con y(0) = 1 => C = 1
   Solución Exacta: y(t) = e^(-t^2)

2. Método de Euler:
   y_{n+1} = y_n + h * f(t_n, y_n)
   donde f(t, y) = -2 * t * y
"""

import math

def f(t, y):
    """Función de la ED: dy/dt = -2*t*y"""
    return -2.0 * t * y

def solucion_exacta(t):
    """Solución analítica obtenida por separación de variables: y(t) = exp(-t^2)"""
    return math.exp(-(t**2))

def metodo_euler(f, t0, y0, h, t_final):
    """
    Aproximación por el método de Euler.
    """
    tiempos = [t0]
    valores_euler = [y0]
    
    t = t0
    y = y0
    
    num_pasos = int((t_final - t0) / h)
    
    for _ in range(num_pasos):
        y = y + h * f(t, y)
        t = round(t + h, 4)
        tiempos.append(t)
        valores_euler.append(y)
        
    return tiempos, valores_euler

if __name__ == "__main__":
    t0 = 0.0
    y0 = 1.0
    h = 0.2
    t_final = 1.0

    tiempos, euler_y = metodo_euler(f, t0, y0, h, t_final)

    print(f"{'t':^8} | {'Euler (Aprox)':^15} | {'Exacta (Analítica)':^20} | {'Error Absoluto':^15}")
    print("-" * 65)

    for t, y_e in zip(tiempos, euler_y):
        y_exact = solucion_exacta(t)
        error = abs(y_exact - y_e)
        print(f"{t:^8.1f} | {y_e:^15.6f} | {y_exact:^20.6f} | {error:^15.6f}")
