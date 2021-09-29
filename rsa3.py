def decompose(n):
    i = 0
    while n & (1 << i) == 0:
        i += 1
    return i, n >> i

def getKeys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    for i in range(2, phi):
        if gcd(phi,i) == 1:
            e = i
            break
    d = multiplicativeInverse(e, phi)
    
    return n, e, d

         