import ipywidgets
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

def funcion(a = -3, b = 1, c = -2):
    fig, ax = plt.subplots()
    x = np.linspace(-10, 10, 200)
    y = np.linspace(-10, 10, 200)
    ax.axis([-10, 10, -10, 10])
    ax.grid(True)
    ax.axvline(linewidth=2, color = 'r')
    ax.axhline(linewidth=2, color = 'r')
    ax.plot(y, (c*(x + a)**2 + b))    
interact(funcion, a = (-10, 10, 1), b = (-10, 10, 1), c = (-5, 5, 1))
    


