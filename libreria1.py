import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from fractions import Fraction
from IPython.display import display, clear_output

def multiplicar_fracciones(a, b, c, d):
    if b==0 or d==0:
        display("Error: No se puede dividir por cero")
    else:
        pro=(a*c)/(b*d)
        pro_str = str(pro)
        print(f'             {a}      {c}        {a*c}',f'\n Producto    ----  +  ----  =    -----    ={pro_str}\n',f'            {b}      {d}        {d*b}')
    

def sumar_fracciones(a, b, c, d):
    if b==0 or d==0:
        display("Error: No se puede dividir por cero")
    else:
        suma=(a*d+c*b)/(b*d)
        suma_str = str(suma)
        #print(f'Suma    ({a}/{b}) + ({c}/{d})    =    {a*d+c*b}/{b*d}   =   {suma_str}')
        print(f'         {a}      {c}        {a*d+c*b}',f'\n Suma    ----  +  ----  =    -----    ={suma_str}\n',f'        {b}      {d}        {d*b}')



# Crear los deslizadores
a_slider = widgets.FloatSlider(min=-10, max=10, step=1, value=1, description='a')
b_slider = widgets.FloatSlider(min=-10, max=10, step=1, value=1, description='b')
c_slider = widgets.FloatSlider(min=-10, max=10, step=1, value=1, description='c')
d_slider = widgets.FloatSlider(min=-10, max=10, step=1, value=1, description='d')

