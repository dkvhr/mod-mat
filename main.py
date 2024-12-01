import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from Examples import examples
from Lissajous import animation

def plot_2d_lissajous(a, b, w1, w2, phase, title):
    t = np.linspace(0, 30 * np.pi, 10000)
    x = a * np.sin(w2 * t)
    y = b * np.sin(w1 * t + phase)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

def plot_custom():
    try:
        a = float(simpledialog.askstring("Input", "Valor do a="))
        b = float(simpledialog.askstring("Input", "Valor do b="))
        w1 = float(simpledialog.askstring("Input", "Valor do w1="))
        w2 = float(simpledialog.askstring("Input", "Valor do w2="))
        phase = float(simpledialog.askstring("Input", "Valor da fase="))
        plot_type = messagebox.askquestion("Animation", "plot animado?")

        if dimension_var.get() == "2D":
            if plot_type == "yes":
                create_lissajous_anim(a, b, w1, w2, phase, "curva de lissajous animada (Custom)")
            else:
                plot_2d_lissajous(a, b, w1, w2, phase, "curva de lissajous em 2D")
        elif dimension_var.get() == "3D":
            # TODO: adicionar coisas 3d
            pass
    except ValueError:
        message.showerror("Error", "Input fornecido eh invalido :(")


def select_preset():
    selection = preset_var.get()
    if selection == "Major Third (2D)":
        plot_type = messagebox.askquestion("animation", "quer um plot animado?")
        if plot_type == "yes":
            animation.create_lissajous_anim(1, 1, np.pi, (5*np.pi)/4, 10, "Major Third animado (2D)")
        else:
            examples.major_third()
    elif selection == "Tritone (2D)":
        plot_type = messagebox.askquestion("Animation", "quer um plot animado?")
        if plot_type == "yes":
            animation.create_lissajous_anim(1, 1, np.pi, (64*np.pi) / 45, 0, "Tritone (2D) animado")
        else:
            examples.tritone()
    elif selection == "Custom":
        plot_custom()

def main():
    root = tk.Tk()
    root.title("Plot de curvas de Lissajous")
    root.geometry("800x400")

    dimension_label = ttk.Label(root, text="Selecione a dimensao: ")
    dimension_label.pack(pady=5)
    global dimension_var
    dimension_var = tk.StringVar(value='2D')
    dimension_frame = ttk.Frame(root)
    dimension_frame.pack()
    ttk.Radiobutton(dimension_frame, text='2D', variable=dimension_var, value='2D').pack(side='left', padx=10)
    ttk.Radiobutton(dimension_frame, text='3D', variable=dimension_var, value='3D').pack(side='left', padx=10)

    preset_label = ttk.Label(root, text="selecione um preset: ")
    preset_label.pack(pady=5)
    global preset_var
    preset_var = tk.StringVar(value='Major Third (2D)')
    preset_menu = ttk.Combobox(root, textvariable=preset_var, values=[
        "Major Third (2D)", "Tritone (2D)", "Butterfly curve(2D)", "Custom"
        ])
    preset_menu.pack()

    plot_button = ttk.Button(root, text="Plot", command=select_preset)
    plot_button.pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()
