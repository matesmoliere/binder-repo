import ipywidgets
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

def parabola(c):
    x = np.linspace(-10, 10, 200)
    y = np.linspace(-10, 10, 200)
    plt.axis([-10, 10, -10, 10])
    #plt.grid(True)
    plt.axvline(linewidth=3, color = 'r')
    plt.axhline(linewidth=2, color = 'r')
    plt.plot(y, (x**2 + c))

interact(parabola, c = (-10, 10))
