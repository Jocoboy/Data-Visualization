import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math


def show_histogram_with_fitting_curve(__lamda__):
    lamda = __lamda__
    bins = np.arange(0, 15, 0.1)
    x = np.random.exponential(lamda, 100000)
    y = lamda*np.exp(-lamda*bins)
    plt.hist(x, bins=6000, color='r', alpha=0.5, edgecolor='y')
    plt.plot(bins, y)
    plt.xlabel('Expectation')
    plt.ylabel('Probability')
    plt.title('Histogram of Exponential Distribution: $\lambda$ = '+str(lamda))
    plt.subplots_adjust(left=0.15)
    # plt.savefig('E_C'+'-'+str(lamda)+'.png')
    plt.show()


show_histogram_with_fitting_curve(0.125)
