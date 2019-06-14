def generate_polygonals(upper, formula):
    """
    Generate polygonal numbers (triangle, square, pentagonals, hexagonals, etc.) from a formula
    The formula needs to have a single integer as input and a single integer as output
    For example, the formula for triangle numbers is:
    lambda n: n * (n + 1) // 2
    Generate all polygonal numbers less than upper
    """

    polygonals = set()
    i = 1
    next = formula(i)
    while next < upper:
        polygonals.add(next)
        i += 1
        next = formula(i)
    return polygonals

def generate_polygonals_recursive(upper, formula):
    """
    Generate polygonal numbers (triangle, square, pentagonals, hexagonals, etc.) from a formula
    The formula needs to have two integers as input and a single integer as output
    The first input is the previous ngonal number, and the second input is the index
    For example, the formula for triangle numbers is:
    lambda prev, n: prev + n
    Generate all polygonal numbers less than upper
    """
    
def sieve(upper):
    """
    Generate all prime numbers less than upper
    Uses the sieve of Eratosthenes
    """

    primes = set()
    composites = set()
    for i in range(2, upper):
        if i not in composites:
            primes.add(i)
            t = 2
            while t * i < upper:
                composites.add(t * i)
                t += 1
    return primes

