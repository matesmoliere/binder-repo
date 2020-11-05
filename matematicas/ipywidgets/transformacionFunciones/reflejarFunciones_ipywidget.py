import ipywidgets
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

def funcion(a = 1):
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2,figsize=(18, 4))
    x = np.linspace(-10, 10, 200)
    y = np.linspace(-10, 10, 200)
    ax1.axis([-10, 10, -10, 10])
    ax1.grid(True)
    ax1.axvline(linewidth=3, color = 'r')
    ax1.axhline(linewidth=2, color = 'r')
    ax1.plot(y, a*(x**2),linewidth=3)
    ax2.axis([-10, 10, -10, 10])
    ax2.grid(True)
    ax2.axvline(linewidth=3, color = 'r')
    ax2.axhline(linewidth=2, color = 'r')
    ax2.plot(y, np.sqrt(a*x),linewidth=3)
interact(funcion, a = (-1,1,1))
