def isPrime(n):
    if n % 2 == 0:
        return False

    for i in range(1, 40):
        a = random.randint(1, n - 1)
        if isComposite(a, n):
            return False
    return True

def isComposite(a, n):
    
    t,d = decompose(n - 1)
    x = pow(a, d, n)
    
    if x == 1 or x == n - 1:
        return False

    for i in range(1, t):
        x0 = x
        x = pow(x0, 2, n)
        if x == 1 and x0 != 1 and x0 != n - 1:
            return True
    if x != 1:
        return True
        
    return False