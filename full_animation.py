import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

A = 1
B = 1
a = 4
b = 5
fps = 120
duration = 1
frames = fps*duration

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 12))
fig.tight_layout(pad=4.0)
#fig, ax = plt.subplots()
ax1.set_aspect('equal')
ax1.set_xlim(-1.5 * A, 1.5 * A)
ax2.set_xlim(0, 2*np.pi)
ax3.set_xlim(0, 2*np.pi)
ax1.set_ylim(-1.5 * B, 1.5 * B)
ax2.set_ylim(-1.5 * A, 1.5 * A)
ax3.set_ylim(-1.5 * B, 1.5 * B)
ax1.axis('off')

ax2.set_title("x(t) = A*sin(a * t + phase)")
ax3.set_title("y(t) = B*sin(b * t)")

line1, = ax1.plot([], [], color='cyan', lw=2)
line2, = ax2.plot([], [], color='blue', lw=2)
line3, = ax3.plot([], [], color='green', lw=2)

# tempo da simulacao
t = np.linspace(0, 2*np.pi, fps * duration)

#pontos iniciais
theta = np.linspace(0, 30 * np.pi, 10000)

def update(frame):
    # fazendo ela "mover"
    phase = 2 * np.pi * frame / frames
    x = A * np.sin(a * theta + phase)
    y = B * np.sin(b * theta)
    line1.set_data(x, y) #curva de lissajous

    x_wave = A * np.sin(a*t + phase)
    y_wave = B * np.sin(b*t)
    line2.set_data(t, x_wave)
    line3.set_data(t, y_wave)
    return line1, line2, line3

ani = FuncAnimation(
    fig, update, frames=frames, blit=True, interval=1000 / fps
)

plt.show()

