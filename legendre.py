def legendre_polynomials(n):
    """
    Generuje listę funkcji lambda, które obliczają wielomiany Legendre'a P_0 do P_n
    Zwracamy funkcje, które przyjmują argument x w [-1, 1]
    """
    P = [lambda x: 1.0]  # P_0(x) = 1
    if n == 0:
        return P

    P.append(lambda x: x)  # P_1(x) = x

    for k in range(2, n + 1):
        # Funkcja tworzy rekurencyjnie P_k na podstawie P_(k-1) i P_(k-2)
        def Pk(x, k=k):
            return ((2 * k - 1) * x * P[k - 1](x) - (k - 1) * P[k - 2](x)) / k
        P.append(Pk)

    return P  # Lista funkcji lambda od P_0 do P_n
