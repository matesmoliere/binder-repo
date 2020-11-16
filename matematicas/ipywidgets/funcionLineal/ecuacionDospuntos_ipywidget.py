import ipywidgets
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np


def ecuacion(x_0 = 0, y_0 = 0, x_1 = 1, y_1 = 0):
    x = np.linspace(-10, 10, 200)    
    y = np.linspace(-10, 10, 200)   
    plt.axis([-10, 10, -10, 10])
    #plt.grid(True)
    plt.axvline(linewidth=3, color = 'r')
    plt.axhline(linewidth=2, color = 'r')
    m = (y_1 - y_0)/(x_1 - x_0)
    plt.plot(y, (m*x + y_0 - m*x_0))
    print('La pendiente m = ', m)

interact(ecuacion, x_0 = (-5, 5, 1), y_0 = (-5, 5, 1), x_1 = (-5, 5, 1), y_1 = (-5, 5, 1))



