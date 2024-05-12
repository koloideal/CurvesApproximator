from scipy.optimize import curve_fit
from numpy import array
import matplotlib.pyplot as plt
import os
import datetime


os.makedirs('../content', exist_ok=True)


def mapping1(mapping1_x, a1, b1, c1): return a1 * mapping1_x ** 2 + b1 * mapping1_x + c1
def mapping2(mapping2_x, a2, b2, c2): return a2 * mapping2_x ** 3 + b2 * mapping2_x + c2
def mapping3(mapping3_x, a3, b3, c3): return a3 * mapping3_x ** 3 + b3 * mapping3_x ** 2 + c3


def approximator(list_y):

    values_y = array(list_y)
    values_x = array(range(len(values_y)))

    args = curve_fit(mapping1, values_x, values_y)[0]
    a, b, c = args[0], args[1], args[2]
    y_fit1 = a * values_x ** 2 + b * values_x + c

    args = curve_fit(mapping2, values_x, values_y)[0]
    a, b, c = args[0], args[1], args[2]
    y_fit2 = a * values_x ** 3 + b * values_x + c

    args = curve_fit(mapping3, values_x, values_y)[0]
    a, b, c = args[0], args[1], args[2]
    y_fit3 = a * values_x ** 3 + b * values_x ** 2 + c

    plt.plot(values_x, values_y, 'bo', label="y - original")
    plt.plot(values_x, y_fit1, label="y = a * x^2 + b * x + c")
    plt.plot(values_x, y_fit2, label="y = a * x^3 + b * x + c")
    plt.plot(values_x, y_fit3, label="y = a * x^3 + b * x^2 * c")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='best', fancybox=True, shadow=True)
    plt.grid(True)
    plt.savefig(f'content/{datetime.datetime.now().strftime("%H-%M-%S")}.png')

    return f'content/{datetime.datetime.now().strftime("%H-%M-%S")}.png'
