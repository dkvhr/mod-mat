import matplotlib.pyplot as plt
import numpy as np

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

