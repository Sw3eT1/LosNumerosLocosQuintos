import numpy as np
import matplotlib.pyplot as plt

def plot_approximation(f, approx, a, b):
    """
    Rysuje wykres funkcji oryginalnej i jej aproksymacji na przedziale [a, b]
    """
    xs = np.linspace(a, b, 500)
    ys_true = [f(x) for x in xs]  # wartości oryginalnej funkcji
    ys_approx = [approx(x) for x in xs]  # wartości aproksymacji

    plt.plot(xs, ys_true, label="f(x)")
    plt.plot(xs, ys_approx, label="Approximated", linestyle="--")
    plt.legend()
    plt.title("Approximation vs Original")
    plt.grid(True)
    plt.show()
