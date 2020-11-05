import ipywidgets
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

def func_plot(c):
    x = np.linspace(-10, 10, 200)
    plt.plot(x, (np.sin(2*np.pi*x) + c))
    plt.axvline(linewidth=3, color = 'r')
    plt.axhline(linewidth=2, color = 'r')

interact(func_plot, c = (-10,10))
