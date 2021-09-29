print("RSA ENCRYPTOR/DECRYPTOR")
print("PLEASE ENTER THE 'p' AND 'q' VALUES BELOW:")
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))

check_p = prime_check(p)
check_q = prime_check(q)

while (((check_p == False) or (check_q == False))):
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    check_p = prime_check(p)
    check_q = prime_check(q)

n = p * q
print("RSA Modulus(n) is:", n)
r = (p - 1) * (q - 1)
print("Eulers Toitent(r) is:", r)

for i in range(1, 1000):
    if (egcd(i, r) == 1):
        e = i
print("The value of e is:", e)

d = multiplicative_inv(e, r)
print("The value of d is:", d)

public = (e, n)
private= (d, n)

print("Private Key is:", private)
print("Public Key is:", public)

message = input("PLEASE ENTER A MESSAGE!")
print("Your message is:", message)

enc_msg = encryption(public, message)
print("Your encrypted message is:", enc_msg)
print("Your decrypted message is:", decryption(private, enc_msg))



