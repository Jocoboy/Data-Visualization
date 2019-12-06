import matplotlib.pyplot as plt
import numpy as np

A = 15
K = 50
ε = 0.1
width, height = 800, 800


def f(x, y):
    return np.sin(x)*np.cos(y)


def g(x, y):
    return np.cos(2*x)*np.sin(y)


def algorithm_1():
    colormap = generate_cmap()
    pixels = np.arange(
        width*height, dtype=np.uint16).reshape(height, width)
    for x_0 in range(width):
        for y_0 in range(height):
            n = 0
            x_n = (2*x_0-width)/A
            y_n = (2*y_0-height)/A
            while(n < K):
                x_n_1 = x_n - f(x_n, y_n)
                y_n_1 = y_n - g(x_n, y_n)
                if(np.sqrt((x_n_1-x_n)**2+(y_n_1-y_n)**2) < ε):
                    break
                n = n+1
                x_n = x_n_1
                y_n = y_n_1
            i = n
            pixels[x_0, y_0] = colormap[i]
    return pixels


def generate_cmap():

    cmap = {i: i*5 for i in range(K)}
    return cmap


def generate_image():

    data = algorithm_1()
    plt.imshow(data)
    plt.savefig("patterns.png")
    plt.show()


if __name__ == "__main__":
    generate_image()
