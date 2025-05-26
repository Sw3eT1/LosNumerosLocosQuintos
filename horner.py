def horner(x, coeffs):
    """
    Algorytm Hornera do obliczania wartości wielomianu dla punktu x
    coeffs - lista współczynników [a_n, a_{n-1}, ..., a_0]
    """
    result = coeffs[0]
    for coeff in coeffs[1:]:
        result = result * x + coeff
    return result
