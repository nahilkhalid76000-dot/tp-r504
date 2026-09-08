def puissance(a, b):
    if not type(a) is int or not type(b) is int:
        raise TypeError("Only integers are allowed")
    if a == 0 and b < 0:
        raise ValueError("0 elevated to a negative power is undefined")
    return a ** b
