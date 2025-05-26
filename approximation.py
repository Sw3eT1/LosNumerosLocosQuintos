import numpy as np
from simpson import simpson
from legendre import legendre_polynomials

def calculate_legendre_coefficients(f, a, b, degree, n_nodes=100):
    """
    Oblicza współczynniki wielomianu Legendre'a dla funkcji f na przedziale [a, b]
    degree - stopień wielomianu
    n_nodes - liczba węzłów do numerycznego całkowania
    """
    legendre = legendre_polynomials(degree)
    coeffs = []

    def map_to_ab(t):
        # Mapowanie punktu t z [-1, 1] na [a, b]
        return 0.5 * (b - a) * t + 0.5 * (b + a)

    for n in range(degree + 1):
        Pn = legendre[n]

        def integrand(t):
            x = map_to_ab(t)  # Przeskalowanie do [a, b]
            return f(x) * Pn(t)  # Funkcja podcałkowa dla współczynnika

        integral = simpson(integrand, -1, 1, n_nodes)
        coeff = (2 * n + 1) / 2 * integral  # Wzór na współczynnik
        coeffs.append(coeff)

    return coeffs, legendre

def evaluate_legendre_approx(x, coeffs, legendre_polys, a, b):
    """
    Oblicza wartość aproksymacji wielomianowej w punkcie x,
    bazując na współczynnikach i wielomianach Legendre'a
    """
    t = (2 * x - a - b) / (b - a)  # mapujemy x z [a, b] na [-1, 1]
    return sum(c * P(t) for c, P in zip(coeffs, legendre_polys))

def approximation_error(f, approx, a, b, n_nodes=100):
    """
    Oblicza błąd aproksymacji jako całkę z kwadratu różnicy f(x) - approx(x)
    """
    def error_func(x):
        return (f(x) - approx(x)) ** 2

    error = simpson(error_func, a, b, n_nodes)
    return error

def auto_approximate(f, a, b, tol, max_degree=20):
    """
    Automatycznie szuka stopnia wielomianu, który spełnia zadaną tolerancję błędu.
    Sprawdza stopnie od 1 do max_degree.
    Jeśli nie znajdzie odpowiedniego stopnia, zwraca najlepszy znaleziony wynik.
    """
    x_vals = np.linspace(a, b, 500)
    best_result = None

    for degree in range(1, max_degree + 1):
        coeffs, legendre_polys = calculate_legendre_coefficients(f, a, b, degree)
        approx = lambda x: evaluate_legendre_approx(x, coeffs, legendre_polys, a, b)

        # Obliczamy błąd w wielu punktach, zabezpieczamy przed NaN/Inf
        errors = []
        for x in x_vals:
            try:
                diff = abs(f(x) - approx(x))
                if np.isnan(diff) or np.isinf(diff):
                    diff = np.inf
            except Exception:
                diff = np.inf
            errors.append(diff)

        errors = np.array(errors)
        max_error = np.max(errors)
        rms_error = np.sqrt(np.mean(errors**2))

        print(f"Degree {degree}, max error = {max_error:.6e}, RMS error = {rms_error:.6e}")

        if max_error < tol:
            return degree, coeffs, legendre_polys, approx, max_error

        # Zapamiętujemy najlepszy wynik (najmniejszy max błąd)
        if best_result is None or max_error < best_result[-1]:
            best_result = (degree, coeffs, legendre_polys, approx, max_error)

    print("Osiągnięto maksymalny stopień bez spełnienia tolerancji.")
    return best_result
