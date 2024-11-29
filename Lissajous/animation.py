import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def create_lissajous_anim(a, b, w1, w2, phase, title):
    t = np.linspace(0, 30*np.pi, 10000)
    x = a*np.sin(w1 * t)
    y = b*np.sin(w2 * t + phase)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(title)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)

    line, = ax.plot([], [], lw=2)

    def update(frame):
        line.set_data(x[:frame], y[:frame])
        return line,

    frames = len(t)
    interval = 20 #ms

    anim = FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)

    plt.show()

