import numpy as np
import matplotlib.pyplot as plt

# Función para agregar flechas en los extremos
def add_arrows(ax, x_min, x_max):
    ax.annotate('', xy=(x_max, 0), xytext=(x_max -1, 0),
                arrowprops=dict(arrowstyle="->", color='black'))
    ax.annotate('', xy=(x_min, 0), xytext=(x_min + 1, 0),
                arrowprops=dict(arrowstyle="->", color='black'))

# Función para crear la gráfica
def plot_inequality_solution(a,b,c):
    x_min, x_max = -10, 10  # Definir el intervalo x
    threshold = (c - b) / a  # Resolver la inecuación 3x + 5 > a
    
    # Crear una figura y eje
    fig, ax = plt.subplots(figsize=(10, 2))
    
    # Graficar la recta numérica
    ax.plot([x_min, x_max], [0, 0], color='black')
    add_arrows(ax, x_min, x_max)
    
    # Agregar una línea vertical en x = threshold
    ax.axvline(x=threshold, color='red', linestyle='--', label=f'x = {threshold:.2f}')
    
    # Puntos que satisfacen la inecuación
    if a < 0:
        solution_points = np.linspace(x_min, threshold, 100)
    else:
        solution_points = np.linspace(threshold, x_max, 100)
    #solution_points = np.linspace(threshold, x_max, 100)
    ax.scatter(solution_points, np.zeros_like(solution_points), color='blue', label=f'Puntos que satisfacen  {a:.2f}x +  {b:.2f} > {c:.2f}')
    
    # Establecer límites y etiquetas del gráfico
    ax.set_xlim(x_min - 1, x_max + 1)
    ax.set_ylim(-0.5, 0.5)
    ax.set_yticks([])
    ax.set_xlabel('x')
    ax.legend()
    ax.set_title(f'Solución de la inecuación  {a:.2f}x +  {b:.2f} > {c:.2f} en el intervalo [{x_min}, {x_max}]')
    
    plt.show()

# Función para resolver la inecuación
    # Función para crear la gráfica de la inecuación cuadrática
# Función para crear la gráfica de la inecuación cuadrática
def plot_inequality_solution2(a, b, c):
    x_min, x_max = -10, 10  # Definir el intervalo x
    x = np.linspace(x_min, x_max, 400)
    y = a * x**2 + b * x + c

    # Encontrar las raíces de la ecuación cuadrática
    discriminant = b**2 - 4*a*c
    
    # Mostrar la gráfica solo si el discriminante es mayor que cero
    if discriminant > 0:
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        roots = sorted([root1, root2])

        # Crear una figura y eje
        fig, ax = plt.subplots(figsize=(10, 2))

        # Graficar la recta numérica
        ax.plot([x_min, x_max], [0, 0], color='black')
        add_arrows(ax, x_min, x_max)

        # Agregar líneas verticales en las raíces
        for root in roots:
            ax.axvline(x=root, color='red', linestyle='--', label=f'x = {root:.2f}')

        # Determinar los puntos que satisfacen la inecuación
        if a > 0:
            solution_points_left = np.linspace(x_min, roots[0], 100)
            solution_points_right = np.linspace(roots[1], x_max, 100)
        else:
            solution_points_left = np.linspace(roots[0], roots[1], 100)
            solution_points_right = []

        ax.scatter(solution_points_left, np.zeros_like(solution_points_left), color='blue', label=f'Puntos que satisfacen {a:.2f}x² + {b:.2f}x + {c:.2f} > 0')
        ax.scatter(solution_points_right, np.zeros_like(solution_points_right), color='blue')

        # Establecer límites y etiquetas del gráfico
        ax.set_xlim(x_min - 1, x_max + 1)
        ax.set_ylim(-0.5, 0.5)
        ax.set_yticks([])
        ax.set_xlabel('x')
        ax.legend()
        ax.set_title(f'Solución de la inecuación {a:.2f}x² + {b:.2f}x + {c:.2f} > 0 en el intervalo [{x_min}, {x_max}]')

        plt.show()

    # Mostrar toda la recta excepto el punto de la raíz si el discriminante es cero
    elif discriminant == 0:
        root = -b / (2*a)

        # Crear una figura y eje
        fig, ax = plt.subplots(figsize=(10, 2))

        # Graficar la recta numérica
        ax.plot([x_min, x_max], [0, 0], color='black')
        add_arrows(ax, x_min, x_max)

        # Determinar los puntos que satisfacen la inecuación excluyendo la raíz
        solution_points_left = np.linspace(x_min, root, 100, endpoint=False)
        solution_points_right = np.linspace(root, x_max, 100, endpoint=False)

        ax.scatter(solution_points_left, np.zeros_like(solution_points_left), color='blue')
        ax.scatter(solution_points_right, np.zeros_like(solution_points_right), color='blue')
        ax.scatter([root], [0], color='black', zorder=5, label=f'Recta sin el punto {root:.2f}')  # Punto negro en la raíz

        # Establecer límites y etiquetas del gráfico
        ax.set_xlim(x_min - 1, x_max + 1)
        ax.set_ylim(-0.5, 0.5)
        ax.set_yticks([])
        ax.set_xlabel('x')
        ax.legend()
        ax.set_title(f'Solución de la inecuación {a:.2f}x² + {b:.2f}x + {c:.2f} > 0 en el intervalo [{x_min}, {x_max}]')

        plt.show()
    
    # Casos donde el discriminante es menor que cero
    else:
        if a < 0:
            print('No existe un punto que satisfaga la ecuación.')
        elif a > 0:
            # Crear una figura y eje
            fig, ax = plt.subplots(figsize=(10, 2))

            # Graficar la recta numérica
            ax.plot([x_min, x_max], [0, 0], color='black')
            add_arrows(ax, x_min, x_max)

            # Graficar toda la recta
            ax.scatter(x, np.zeros_like(x), color='blue', label=f'Toda la recta para {a:.2f}x² + {b:.2f}x + {c:.2f}')

            # Establecer límites y etiquetas del gráfico
            ax.set_xlim(x_min - 1, x_max + 1)
            ax.set_ylim(-0.5, 0.5)
            ax.set_yticks([])
            ax.set_xlabel('x')
            ax.legend()
            ax.set_title(f'Solución de la inecuación {a:.2f}x² + {b:.2f}x + {c:.2f} > 0 en el intervalo [{x_min}, {x_max}]')

            plt.show()