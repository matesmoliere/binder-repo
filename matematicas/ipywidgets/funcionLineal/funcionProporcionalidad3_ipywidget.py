import ipywidgets
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

def ecuacion(m = 1, n = 0):
    x = np.linspace(-10, 10, 200)
    y = np.linspace(-10, 10, 200)
    plt.axis([-10, 10, -10, 10])
    #plt.grid(True)
    plt.axvline(linewidth=3, color = 'r')
    plt.axhline(linewidth=2, color = 'r')
    plt.plot(y, (m*x + n))

interact(ecuacion, m = (-3, 3, 0.25), n = (-3, 3, 0.25))
