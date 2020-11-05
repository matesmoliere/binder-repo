import ipywidgets
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

def func_plot(c = 1):
    x = np.linspace(-3, 3, 200)
    plt.axvline(linewidth=3, color = 'r')
    plt.axhline(linewidth=2, color = 'r')
    plt.plot(x, np.sin(c*x))

interact(func_plot, c = (0, 3, 0.1))
