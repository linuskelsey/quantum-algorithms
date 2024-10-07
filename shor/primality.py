import math
# Function to run the Miller-Rabin test
def primality(n):
    if n % 2 == 0:
        return 0
    # get s>0 and d>0 odd s.t. n-1=2^s * d
    s, a = 0, n-1
    while a % 2 == 0:
        a = a / 2
        s += 1
    d = a
    # Miller-Rabin
    for a in range(2, min(n-2, math.floor(2*(math.log(n)**2)))):
        x = a**d % n
        for i in range(s):
            y = x**2 % n
            if y == 1 and x != 1 and x != n-1:
                return 0
            x = y
        if y != 1:
            return 0
    return 1