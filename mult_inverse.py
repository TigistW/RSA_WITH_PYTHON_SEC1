
def exteucliedan(a, b):
    if (a % b == 0):
        return (b, 0, 1)
    else:
        gcd, s, t = exteucliedan(b, a % b)
        s = s - ((a // b) * t)
        return (gcd, t, s)
def multiplicative_inv(e, r):
    gcd, s, _ = exteucliedan(e, r)
    if (gcd != 1):
        return None
    else:
        if (s < 0):
            print(s%r)
        elif (s > 0):
            print(s)
        return s % r