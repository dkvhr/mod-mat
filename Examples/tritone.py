import matplotlib.pyplot as plt
import numpy as np

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

