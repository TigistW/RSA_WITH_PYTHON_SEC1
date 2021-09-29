def multiplicativeInverse(e, phi):
    return extendedEuclid(e, phi)[1] % phi

def extendedEuclid(a, b):
    if b == 0:
        return a, 1, 0
    else: 
        d2, x2, y2 = extendedEuclid(b, a % b)
        d, x, y = d2, y2, x2 - (a // b) * y2
        return d, x, y