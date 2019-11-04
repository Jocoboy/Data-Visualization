import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm


def show_histogram(__mu__=0, __sigma__=1, __sampleNo__=1000):
    mu, sigma = __mu__, __sigma__
    sampleNo = __sampleNo__
    '''
    Seed the generator.
    This method is called when RandomState is initialized. It can be called again to re-seed the generator.
    # Parameters:
    # seed[int/array_like](optional) : Seed for RandomState. Must be convertible to 32 bit unsigned integers.
    '''
    np.random.seed(0)
    '''
    Draw random samples from a normal (Gaussian) distribution.
    # Parameters:
    # loc[float/array_like of floats] : Mean (“centre”) of the distribution.
    # scale[float/array_like of floats] : Standard deviation (spread or “width”) of the distribution.
    # size[int/tuple of ints](optional) : Output shape. If the given shape is, e.g., (m, n, k), then m * n * k samples are drawn.
    '''
    s = np.random.normal(mu, sigma, sampleNo)
    '''
    # Parameters:
    # x : (n,) array or sequence of (n,) arrays
    # bins[int/sequence/str](optional) : If an integer is given, bins + 1 bin edges are calculated and returned, consistent with numpy.histogram.
    # normed[bool](optional) : Deprecated; use the density keyword argument instead.
    # density[bool](optional) : If True, the first element of the return tuple will be the counts normalized to form a probability density
      Default is None for both normed and density. If either is set, then that value will be used. If neither are set, then the args will be treated as False.
      If both density and normed are set an error is raised.
    '''
    plt.hist(s, bins=100, density=True)
    plt.xlabel('Expectation')
    plt.ylabel('Probability')
    plt.title('Histogram of Normal Distribution: $\mu = ' +
              str(mu)+'$, $\sigma='+str(sigma)+'$')
    '''Display a figure.'''
    plt.savefig('histogram'+str(mu) +
                '-'+str(sigma)+'-'+str(sampleNo)+'.png')
    plt.show()


def show_histogram_with_fitting_curve(__mu__=0, __sigma__=1, __sampleNo__=1000):
    mu, sigma = __mu__, __sigma__
    sampleNo = __sampleNo__
    '''Return a sample (or samples) from the “standard normal” distribution.'''
    x = mu + sigma * np.random.randn(sampleNo)
    '''
    # Returns:
    # n[array/list of arrays] : The values of the histogram bins.
    # bins[array] : The edges of the bins.
    # patches[list/list of lists] : Silent list of individual patches used to create the histogram or list of such list if multiple input datasets.
    '''
    n, bins, patches = plt.hist(
        x, bins=50, density=True, facecolor='red', alpha=0.5)
    '''Probability density function.'''
    y = norm.pdf(bins, mu, sigma)
    '''
    Plot y versus x as lines and/or markers.
    # Parameters:
    # [x],y[array-like/scalar] :
    # fmt[str](optional) : A format string.
      A format string consists of a part for color, marker and line:
      fmt = '[marker][line][color]'
      e.g. 'r--'
    '''
    plt.plot(bins, y, 'r--')
    plt.xlabel('Expectation')
    plt.ylabel('Probability')
    plt.title('Histogram of Normal Distribution: $\mu = 0$, $\sigma=1$')
    '''Tune the subplot layout.'''
    plt.subplots_adjust(left=0.15)
    '''Display a figure.'''
    plt.savefig('histogram_with_fitting_curve'+str(mu) +
                '-'+str(sigma)+'-'+str(sampleNo)+'.png')
    plt.show()


show_histogram(0, 1)
# show_histogram_with_fitting_curve(0, 1, 1000000)
