###returns wheter or not n is a Prime number
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

###returns the next Prime number after n
def nextprime(n):
    k = n + 1
    while not is_prime(k):
        k = k + 1
    return k

###returns a list of all primes between start and end
def primelist(start, end, show = False):
    k = nextprime(start)
    primes = list()
    while(k <= end):
        primes.append(k)
        k = nextprime(k)
    if show:
        for i in range(len(primes)):
            print(primes[i])
    else:
        return primes

### returns a Dictionary of all Prime Factors
def pfactor(n, show = False):
    factors = dict()
    value = n
    factor = 2
    factors.update({2:0})
    while not value == 1:
        remainder = value % factor
        if remainder == 0:
            value = value/factor
            factors[factor] = factors[factor] + 1
        else:
            factor = nextprime(factor)
            factors.update({factor : 0})
    finalfactors = {key: value for key, value in factors.items() if not value == 0}
    if show:
        text = ""
        for el in factors.keys():
            if not factors[el] == 0:
                text = text + str(el) + "^" + str(factors[el]) + " * "
        print(str(n) + " = " + text[: -3])
    return finalfactors
