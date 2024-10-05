# Simple implementation of Euclid's algorithm
def gcd(a,b):
    r = a % b
    while r:
        a = b
        b = r
        r = a%b
    return b