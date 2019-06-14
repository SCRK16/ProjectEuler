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
    
    polygonals = set()
    i = 1
    next = 1
    while next < upper:
        polygonals.add(next)
        i += 1
        next = formula(next, i)
    return polygonals

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

def digits(n, convert=False):
    """
    The digits of n as a list
    """
    return [int(x) for x in str(n)] if convert else list(str(n))

def is_palindrome(l):
    """
    Check if a list is a palindrome
    """
    return l == list(reversed(l))

def factorial(n):
    """
    Calculate n!
    If n! needs to be calculated for many different n,
    use factorial_memory instead to cache results
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def factorial_memory(n, memory):
    """
    Factorial with memory
    Prevents unneeded duplicate calculations by checking the memory for previous results
    """
    if n in memory:
        return memory[n]
    if n == 0 or n == 1:
        return 1
    memory[n] = n * factorial_memory(n - 1, memory)
    return memory[n]

def wordscore(word):
    """
    Calculate the wordscore of a word
    The score of a letter is its position in the alphabet
    The score of a word is the sum of the scores of its letters
    """
    score = 0
    for c in word:
        score += ord(c) - ord('A') + 1
    return score

def concatenate(ns):
    """
    Concatenate a list of numbers
    """
    return int(''.join([str(n) for n in ns]))
