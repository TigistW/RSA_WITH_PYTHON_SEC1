from math import gcd
import random
from random import randint


def encodeMessage(msg):
    encodedMsg = 0
    for char in msg:
        encodedMsg = encodedMsg << 8
        encodedMsg = encodedMsg ^ ord(char)
    return encodedMsg

def getRandomPrime(primeSize):
    x = randint(1 << (primeSize - 1), (1 << primeSize) - 1)
    while not (isPrime(x)):
        x = randint(1 << (primeSize - 1), (1 << primeSize) - 1) 
    return x