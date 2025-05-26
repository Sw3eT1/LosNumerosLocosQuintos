import numpy as np

def simpson(f, a, b, n):
    """
    Metoda Simpsona do numerycznego całkowania funkcji f na przedziale [a, b]
    n - liczba podprzedziałów (musimy mieć parzystą liczbę podprzedziałów)
    Zwraca wartość całki obliczoną metodą Simpsona
    """
    if n % 2 == 1:
        n += 1  # Upewniamy się, że n jest parzyste
    deltaX = (b - a) / n
    x = np.linspace(a, b, n + 1)  # węzły podziału
    fx = [f(xi) for xi in x]  # wartości funkcji w węzłach
    S = fx[0] + fx[-1] + 4 * sum(fx[1:-1:2]) + 2 * sum(fx[2:-2:2])
    return deltaX * S / 3
