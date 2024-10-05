# Function to determine if a number is of the form a^b, a≥1, b≥2.
def powerCheck(a):
    b=2
    # while condition makes an efficiency as numbers tested at
    # this stage of Shor's algorithm are guaranteed not even.
    while round(a ** (1.0/b),2) >= 3:
        # approximation methods to compute the roots sometimes give .999...
        # as a trailing decimal.
        if round((a ** (1.0/b)), 10) % 1 == 0:
            return b, round(a ** (1.0/b), 0)
        b += 1

    return 0