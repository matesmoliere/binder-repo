import ipywidgets
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

def funcion(c = 1, c1 = 0.5):
    fig, ax = plt.subplots()
    x = np.linspace(-10, 10, 200)
    y = np.linspace(-10, 10, 200)
    ax.axis([-10, 10, -10, 10])
    ax.grid(True)
    ax.axvline(linewidth=2, color = 'r')
    ax.axhline(linewidth=2, color = 'r')
    ax.plot(y, (c*(x**2)))
    ax.plot(y, (c1*(x**2)))
interact(funcion, c = (1,10,1), c1 = (0.01, 1, 0.1))
    


