def divisors(n):
    """
    Calculate the proper divisors of n
    Lazy implementation
    """
    result = []
    for i in range(1, n):
        if n % i == 0:
            result.append(i)
    return result

def amicable(n):
    """
    Checks if n is part of a pair of amicable numbers
    Return type: (bool, int)
    The int is the sum of the proper divisors of n, called m
    The bool is True if and only if (n, m) form an amicable pair
    Meaning: The sum of the proper divisors of m is n

    Calculating m this way prevents a second loop over range(bound)!    
    """
    dn = divisors(n)
    m = sum(dn)
    dm = divisors(m)
    if sum(dm) == n and m != n:
        return True, m
    return False, m

listed = []
tried = set()
bound = 10000

for i in range(bound):
    if i not in tried:
        is_amicable, other = amicable(i)
        tried.add(i)
        tried.add(other)
        if is_amicable:
            listed.append((i, other))
            amicables.add(i)
            amicables.add(other)

print(listed)
print(sum(sum(x) for x in listed))
