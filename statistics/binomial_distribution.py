import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import binom


def show_histogram_with_fitting_curve(__n__, __p__):
    n, p = __n__, __p__
    bins = np.arange(0,10)
    x = np.random.binomial(n, p, size=10000)
    y = binom.pmf(bins,n,p)
    plt.plot(bins,y)
    plt.hist(x, bins=10, density=True, color='r', alpha=0.5, edgecolor='b')
    plt.xlabel('Expectation')
    plt.ylabel('Probability')
    plt.title('Histogram of Binomial Distribution: n = ' +
              str(n)+', p = '+str(p))
    plt.subplots_adjust(left=0.15)
    # plt.savefig('B_C' + '-' + str(n)+'-'+str(p)+ '.png')
    plt.show()


show_histogram_with_fitting_curve(10, 0.5)
