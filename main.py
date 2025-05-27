from time import sleep
from horner import horner
from approximation import *  # Importujemy funkcje do aproksymacji
from plotter import plot_approximation  # Funkcja do rysowania wykresów

# Definicja dostępnych funkcji do aproksymacji, każda z opisem i funkcją lambda
functions = {
    "a": ("f(x) = 2x + 1", lambda x: horner(x, [2, 1])),
    "b": ("f(x) = |x - 2|", lambda x: abs(horner(x, [1, -2]))),
    "c": ("f(x) = x^3 - 4x^2 + x + 6", lambda x: horner(x, [1, -4, 1, 6])),
    "d": ("f(x) = sin(x)", lambda x: np.sin(x)),
    "e": ("f(x) = sin(x^2)", lambda x: np.sin(x**2))
}

def choose_function():
    # Pokazuje menu wyboru funkcji dla użytkownika i pobiera wybór
    print("Choose a function:")
    for key, (desc, _) in functions.items():
        print(f" {key}) {desc}")
    while True:
        val = input("Select your option: ").lower()
        if val in functions:
            return functions[val]
        print("Invalid input. Try again.")  # Jeśli zły wybór, prosi ponownie
        sleep(1)

def main():
    desc, f = choose_function()  # Wybieramy funkcję
    print(f"Selected: {desc}")

    # Pobieramy od użytkownika przedział aproksymacji
    a = float(input("Enter interval start a: "))
    b = float(input("Enter interval end b: "))

    mode = input("Manual degree (s) or target error (b)? ").lower()  # Tryb aproksymacji

    if mode == "s":
        # Użytkownik podaje ręcznie stopień wielomianu
        degree = int(input("Enter polynomial degree: "))
        coeffs, legendre_polys = calculate_legendre_coefficients(f, a, b, degree)
        approx = lambda x: evaluate_legendre_approx(x, coeffs, legendre_polys, a, b)
        error = approximation_error(f, approx, a, b)
    else:
        # Użytkownik podaje tolerancję błędu - aproksymujemy automatycznie
        tol = float(input("Enter target error (e.g. 0.001): "))
        degree, coeffs, legendre_polys, approx, error = auto_approximate(f, a, b, tol)

    print(f"\nDone! Degree = {degree}, Error = {error:.6f}")
    plot_approximation(f, approx, a, b, degree, desc, error)  # Rysujemy wykres oryginału i aproksymacji

if __name__ == "__main__":
    main()  # Punkt startowy programu
