import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

A = 1
B = 1
a = 1
b = 1
fps = 120
duration = 1
frames = fps * duration

t = np.linspace(0, 2 * np.pi, fps * duration)

theta = np.linspace(0, 30 * np.pi, 10000)

def create_animation(x_data_func, y_data_func, xlim, ylim, title, color, filename):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_title(title)
    ax.axis('off')

    line, = ax.plot([], [], color=color, lw=2)

    def update(frame):
        phase_x = 2 * np.pi * frame / frames
        phase_y = 4 * np.pi * frame/frames
        x = x_data_func(frame, phase_x)
        y = y_data_func(frame, phase_y)
        line.set_data(x, y)
        return line,

    ani = FuncAnimation(
        fig, update, frames=frames, blit=True, interval=1000 / fps
    )

    ani.save(filename, writer=PillowWriter(fps=fps))
    plt.close(fig)

create_animation(
    x_data_func=lambda frame, phase_x: A * np.sin(a * theta + phase_x),
    y_data_func=lambda frame, phase_y: B * np.sin(b * theta + phase_y),
    xlim=(-1.5 * A, 1.5 * A),
    ylim=(-1.5 * B, 1.5 * B),
    title="Lissajous Curve",
    color='cyan',
    filename="lissajous_curve.gif"
)

create_animation(
    x_data_func=lambda frame, phase_x: t,
    y_data_func=lambda frame, phase_x: A * np.sin(a * t + phase_x),
    xlim=(0, 2 * np.pi),
    ylim=(-1.5 * A, 1.5 * A),
    title="x(t) = A*sin(a*t + phase)",
    color='blue',
    filename="x_wave.gif"
)

create_animation(
    x_data_func=lambda frame, phase_y: t,
    y_data_func=lambda frame, phase_y: B * np.sin(b * t + phase_y),
    xlim=(0, 2 * np.pi),
    ylim=(-1.5 * B, 1.5 * B),
    title="y(t) = B*sin(b*t + phase)",
    color='green',
    filename="y_wave.gif"
)

