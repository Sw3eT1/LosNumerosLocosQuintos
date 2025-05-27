import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D  # <-- to potrzebne

def plot_approximation(f, approx, a, b, degree, desc, error):
    """
    Rysuje wykres funkcji oryginalnej i jej aproksymacji na przedziale [a, b]
    """
    xs = np.linspace(a, b, 500)
    ys_true = [f(x) for x in xs]  # wartości oryginalnej funkcji
    ys_approx = [approx(x) for x in xs]  # wartości aproksymacji

    plt.plot(xs, ys_true, label=f'f(x): {desc}')
    plt.plot(xs, ys_approx, label=f'Approximated for polynomial degree: {degree}', linestyle="--")

    # Tworzenie pustego obiektu do legendy
    fake_line = Line2D([0], [0], color='none', label=f'Approximation error: {error:.6f}')
    plt.legend(handles=plt.gca().get_legend_handles_labels()[0] + [fake_line],
               fontsize=8, loc='upper right')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Approximation vs Original")
    plt.grid(True)
    plt.show()
