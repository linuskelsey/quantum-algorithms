# Function to determine if a number is of the form a^b, a≥1, b≥2.
def powerCheck(a):
    b=2
    # while condition makes an efficiency as numbers tested at this stage
    # of Shor's algorithm are guaranteed not even.
    while a ** (1.0/b) >= 3:
        if round((a ** (1.0/b)), 10) % 1 == 0:
            return b, round(a ** (1.0/b), 0)
        b += 1

    return 0