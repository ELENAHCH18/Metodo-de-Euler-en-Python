# Aproximación de Ecuación Diferencial Separable con el Método de Euler

## Descripción del proyecto

Este proyecto resuelve la ecuación diferencial separable:

$$
\frac{dy}{dt} = y \cdot t, \quad y(0) = 1
$$

utilizando dos métodos:

- **Solución analítica** mediante separación de variables, que da la solución exacta:

$$
y(t) = e^{\frac{t^2}{2}}
$$

- **Método numérico de Euler** para aproximar la solución en el intervalo $$ t \in [1] $$ con paso $$ h = 0.2 $$.

El script `eluer.py` calcula ambas soluciones, imprime los valores y genera una gráfica comparativa que se guarda como `grafica_euler.png`.

---

## Estructura del repositorio

```
euler-separable-ode/
│
├── eluer.py               # Script principal con la implementación
├── README.md              # Este archivo
├── requirements.txt       # Dependencias del proyecto
└── .gitignore             # Archivos y carpetas ignoradas por Git
```

---

## Cómo configurar y ejecutar

### 1. Clonar el repositorio

```bash
git clone 
cd euler-separable-ode
```

### 2. Crear y activar entorno virtual (recomendado)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Ejecutar el script

```bash
python eluer.py
```

Se imprimirán los valores aproximados y exactos, y se generará la imagen `grafica_euler.png` con la comparación.

---

## Archivos importantes

- **eluer.py**: Código Python que implementa el método de Euler y calcula la solución exacta.
- **requirements.txt**: Contiene las librerías `numpy` y `matplotlib` necesarias.
- **.gitignore**: Ignora archivos temporales, entorno virtual y la imagen generada para evitar subirlos al repositorio.

---

## Notas adicionales

- El script está configurado para guardar la gráfica en un archivo PNG en lugar de mostrarla en pantalla, para evitar errores en entornos sin interfaz gráfica.
- Puedes abrir `grafica_euler.png` con cualquier visor de imágenes para ver la comparación visual.
- Para desactivar el entorno virtual, usa el comando `deactivate`.

---

Si tienes dudas o quieres contribuir, ¡bienvenido! Puedes abrir un issue o un pull request.
