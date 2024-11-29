import numpy as np
import matplotlib.pyplot as plt

def major_third():
    t = np.linspace(0, 30*np.pi, 10000)

    a, b = 1, 1
    w1 = np.pi
    w2 = (5*np.pi)/4
    phase = 10

    y = a * np.sin(w1 * t + phase)
    x = b * np.sin(w2 * t)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title('2d lissajous major third')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.axis('equal')
    plt.grid(True)

    plt.show()

def tritone():
    t = np.linspace(0, 30*np.pi, 10000)

    a, b = 1, 1
    w1 = np.pi
    w2 = (64*np.pi)/45
    phase = 0

    y = a * np.sin(w1 * t + phase)
    x = b * np.sin(w2 * t)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title('2d butterfly curve')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.axis('equal')
    plt.grid(True)

    plt.show()

def butterfly_3d():
    ax = plt.figure().add_subplot(projection='3d')

    t = np.linspace(0, 12*np.pi, 1000)

    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np.sin(t/12)**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np.sin(t/12)**5)
    z = t

    ax.plot(x, y, z, label='butterfly curve')
    ax.legend()

    plt.show()

def butterfly_2d():
    t = np.linspace(0, 12*np.pi, 1000)

    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np.sin(t/12)**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np.sin(t/12)**5)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='2d butterfly curve')
    plt.title('2d butterfly curve')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.axis('equal')
    plt.grid(True)

    plt.show()

def simple_parametric():
    ax = plt.figure().add_subplot(projection='3d')

    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z**2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)

    ax.plot(x, y, z, label='curva parametrica')
    ax.legend()

    plt.show()


