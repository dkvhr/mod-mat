import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')

t = np.linspace(0, 12*np.pi, 1000)

x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np.sin(t/12)**5)
y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np.sin(t/12)**5)
z = t

ax.plot(x, y, z, label='butterfly curve')
ax.legend()

plt.show()
