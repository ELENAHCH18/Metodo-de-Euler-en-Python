import numpy as np
import matplotlib
# Forzamos el backend 'Agg' que no requiere interfaz gráfica
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def f(t, y):
    return y * t

# Condición inicial y parámetros
t0 = 0
y0 = 1
h = 0.2
t_final = 1

# Puntos de evaluación
t_values = np.arange(t0, t_final + h, h)
y_euler = np.zeros(len(t_values))
y_euler[0] = y0

# Método de Euler
for i in range(1, len(t_values)):
    y_euler[i] = y_euler[i-1] + h * f(t_values[i-1], y_euler[i-1])

# Solución exacta para comparar
y_exact = np.exp(0.5 * t_values**2)

# Resultados
print("t\tEuler\t\tExacta")
for t, y_num, y_ex in zip(t_values, y_euler, y_exact):
    print(f"{t:.1f}\t{y_num:.6f}\t{y_ex:.6f}")

# Graficamos la solución aproximada y exacta
plt.plot(t_values, y_euler, 'o-', label='Euler')
plt.plot(t_values, y_exact, 's--', label='Exacta')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Método de Euler vs Solución Exacta')
plt.legend()
plt.grid(True)

# Guardamos la gráfica en archivo PNG
plt.savefig('grafica_euler.png')
print("Gráfica guardada como 'grafica_euler.png'")

# No usamos plt.show() para evitar errores en entornos sin GUI
