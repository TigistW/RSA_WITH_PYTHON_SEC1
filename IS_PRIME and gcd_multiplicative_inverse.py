def prime_check(a):
    if (a == 2):
        return True
    elif ((a < 2) or ((a % 2) == 0)):
        return False
    elif (a > 2):
        for i in range(2, a):
            if not (a % i):
                return False
    return True

def egcd(e, r):
    while (r != 0):
        REM=e%r
        #e, r = r, e % r
        e=r
        r=REM
    return e
