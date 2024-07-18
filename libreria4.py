# libreria.py
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets

def grafica_recta(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    # Calcular la pendiente (m) y la intersección con el eje y (b) de la recta
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1

    # Generar valores de x para graficar la recta
    x = np.linspace(min(x1, x2) - 1, max(x1, x2) + 1, 400)
    y = m * x + b

    # Graficar la recta y los puntos
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label=f'y = {m:.2f}x + {b:.2f}')
    plt.scatter([x1, x2], [y1, y2], color='red')
    plt.text(x1, y1, f'  ({x1}, {y1})', fontsize=12, ha='left')
    plt.text(x2, y2, f'  ({x2}, {y2})', fontsize=12, ha='left')

    # Configurar el gráfico para mostrar las 4 regiones del plano cartesiano
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim(min(x1, x2) - 2, max(x1, x2) + 2)
    plt.ylim(min(y1, y2) - 2, max(y1, y2) + 2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Recta que une los puntos')
    plt.show()

def grafica_recta_pendiente_punto(m, p):
    x1, y1 = p

    # Generar valores de x para graficar la recta
    x = np.linspace(x1 - 5, x1 + 5, 400)
    y = m * x + (y1 - m * x1)

    # Graficar la recta y el punto
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label=f'y = {m:.2f}x + ({y1 - m * x1:.2f})')
    plt.scatter([x1], [y1], color='red')
    plt.text(x1, y1, f'  ({x1}, {y1})', fontsize=12, ha='left')

    # Configurar el gráfico para mostrar las 4 regiones del plano cartesiano
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim(x1 - 5, x1 + 5)
    plt.ylim(y1 - 5, y1 + 5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Recta con pendiente y punto dado')
    plt.show()

def grafica_dos_rectas(m1, p1, m2, p2):
    x1, y1 = p1
    x2, y2 = p2

    # Generar valores de x para graficar ambas rectas
    x = np.linspace(-10, 10, 400)  # Extendemos el rango de x para ver mejor la intersección
    
    # Calcular las rectas
    y1 = m1 * x + (p1[1] - m1 * p1[0])
    y2 = m2 * x + (p2[1] - m2 * p2[0])

    # Graficar ambas rectas y los puntos
    plt.figure(figsize=(8, 8))
    plt.plot(x, y1, label=f'l1: y = {m1:.2f}x + ({p1[1] - m1 * p1[0]:.2f})')
    plt.plot(x, y2, label=f'l2: y = {m2:.2f}x + ({p2[1] - m2 * p2[0]:.2f})')
    plt.scatter([p1[0]], [p1[1]], color='red')
    plt.scatter([p2[0]], [p2[1]], color='blue')
    plt.text(p1[0], p1[1], f'  ({p1[0]}, {p1[1]})', fontsize=12, ha='left', color='red')
    plt.text(p2[0], p2[1], f'  ({p2[0]}, {p2[1]})', fontsize=12, ha='left', color='blue')

    # Configurar el gráfico para mostrar las 4 regiones del plano cartesiano
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.gca().set_aspect('equal', adjustable='box')  # Esto asegura que las unidades de x e y sean iguales
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Rectas con pendiente y punto dado')
    plt.show()

  
def grafica_parabola(p1, p2, p3): #para graficar la parabola que pasa por tres puntos
    # Extraer las coordenadas de los puntos
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # Resolver el sistema de ecuaciones para encontrar los coeficientes de la parábola
    A = np.array([
        [x1**2, x1, 1],
        [x2**2, x2, 1],
        [x3**2, x3, 1]
    ])
    B = np.array([y1, y2, y3])
    coef = np.linalg.solve(A, B)

    # Generar valores de x para graficar la parábola
    x = np.linspace(-10, 10, 400)  # Rango fijo de -10 a 10
    y = coef[0] * x**2 + coef[1] * x + coef[2]

    # Graficar la parábola y los puntos
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label=f'y = {coef[0]:.2f}x^2 + {coef[1]:.2f}x + {coef[2]:.2f}')
    plt.scatter([x1, x2, x3], [y1, y2, y3], color='red')
    plt.text(x1, y1, f'  ({x1}, {y1})', fontsize=12, ha='left')
    plt.text(x2, y2, f'  ({x2}, {y2})', fontsize=12, ha='left')
    plt.text(x3, y3, f'  ({x3}, {y3})', fontsize=12, ha='left')

    # Configurar el gráfico para mostrar las 4 regiones del plano cartesiano
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim(-10, 10)  # Rango fijo de -10 a 10
    plt.ylim(min(y1, y2, y3) - 2, max(y1, y2, y3) + 2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Parábola que pasa por tres puntos')
    plt.show()

def grafica_parabola_can(a, h, k):
    # Generar valores de x para graficar la parábola
    x = np.linspace(h - 10, h + 10, 400)  # Rango centrado en h
    y = a * (x - h)**2 + k

    # Graficar la parábola
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label=f'$y = {a}(x - {h})^2 + {k}$')

    # Etiquetar el vértice
    plt.scatter(h, k, color='red')  # Dibuja un punto en el vértice
    plt.text(h, k, f'  ({h}, {k})', fontsize=12, ha='left')  # Etiqueta el vértice
    
    # Configurar el gráfico para mostrar las 4 regiones del plano cartesiano
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim(h - 10, h + 10)  # Rango centrado en h
    plt.ylim(k - 10, k + 10)  # Rango centrado en k
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Parábola en la forma $y=a(x-h)^2 + k$')
    plt.show()



# Crear los deslizadores
a_slider = widgets.FloatSlider(min=-10, max=10, step=0.1, value=-1, description='a')
h_slider = widgets.FloatSlider(min=-10, max=10, step=0.1, value=2, description='h')
k_slider = widgets.FloatSlider(min=-10, max=10, step=0.1, value=3, description='k')

# Función para actualizar la gráfica de la parábola en forma canonica
def update_grafica(a, h, k):
    grafica_parabola_can(a, h, k)    

    


 

# Función para graficar la función cuadrática
def grafica_funcion_cuadratica(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Gráfica de la función cuadrática en forma general')
    plt.show()

# Crear los deslizadores
a_slider = widgets.FloatSlider(min=-10, max=10, step=0.1, value=1, description='a')
b_slider = widgets.FloatSlider(min=-10, max=10, step=0.1, value=0, description='b')
c_slider = widgets.FloatSlider(min=-10, max=10, step=0.1, value=0, description='c')

# Función para actualizar la gráfica
def update_grafica_cuad(a, b, c):
    grafica_funcion_cuadratica(a, b, c)