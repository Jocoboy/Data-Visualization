import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm


def show_histogram(__lamda__, __k__):
    lamda, k = __lamda__, __k__
    pillar = 15
    x = np.random.poisson(lam=lamda, size=k)
    n = plt.hist(x, bins=pillar, density=True, range=[
                 0, pillar], color='yellow', alpha=0.5)
    plt.xlabel('Expectation')
    plt.ylabel('Probability')
    plt.title('Histogram of Possion Distribution: $\lambda$ = '+str(lamda))
    plt.subplots_adjust(left=0.15)
    plt.savefig('histogram'+str(lamda)+'-' + str(k) + '.png')
    plt.show()


def show_histogram_with_fitting_curve(__lamda__, __k__):
    lamda, k = __lamda__, __k__
    '''
    Draw samples from a Poisson distribution.
    # Parameters:
    # lam[float/array_like of floats] : Expectation of interval, should be >= 0. A sequence of expectation intervals must be broadcastable over the requested size.
    # size[int/tuple of ints] (optional) : Output shape. 
    '''
    x = np.random.poisson(lam=lamda, size=k)
    pillar = 15
    n = plt.hist(x, bins=pillar, density=True, range=[
                 0, pillar], color='green', alpha=0.5)
    plt.plot(n[1][0:pillar], n[0], 'g')
    plt.xlabel('Expectation')
    plt.ylabel('Probability')
    plt.title('Histogram of Possion Distribution: $\lambda$ = '+str(lamda))
    plt.subplots_adjust(left=0.15)
    '''
    Turn the axes grids on or off.
    Set the axes grids on or off; b is a boolean. (For MATLAB compatibility, b may also be a string, ‘on’ or ‘off’.)
    If b is None and len(kwargs)==0, toggle the grid state.
    '''
    plt.grid()
    plt.savefig('histogram_with_fitting_curve' +
                str(lamda)+'-' + str(k) + '.png')
    plt.show()


show_histogram(5, 1000)
# show_histogram_with_fitting_curve(5, 10000)
