msg = "MY BIGGEST SECRET!"
modulusSize = 1024
primeSize = modulusSize // 2

p = getRandomPrime(primeSize)
q = getRandomPrime(primeSize)
print("p = ", p)
print(" q = ", q)

while p == q:
    q = getRandomPrime(primeSize)

n, e, d = getKeys(p, q)

encodedMsg = encodeMessage(msg)
encryptedMsg = pow(encodedMsg, e, n)
decryptedMsg = pow(encryptedMsg, d, n)


print("Public key (e, n):")
print("\te = ", e)
print("\tn = ", n)
print("\nPrivate key (d, n):")
print("\td = ", d)
print("\tn = ", n)
print("\nOriginal message string:\n\t", msg)
print("\nInteger encoded message:\n\t", encodedMsg)
print("\nEncrypted message:\n\t", encryptedMsg)
print("\nDecrypted message:\n\t", decryptedMsg)
if encodedMsg == decryptedMsg:
    print("\nThe decrypted message and the original encoded message match.")