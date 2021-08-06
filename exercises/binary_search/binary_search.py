from exercises.binary_search import variables


def search(n):
    _min = 1
    _max = 10_000_000_000_000_000
    while True:
        guess = (_min + _max) // 2
        if guess > n:
            _max = guess
        elif guess < n:
            _min = guess
        else:
            return guess


def is_prime(n):
    primes = variables.primes
    while True:
        half = len(primes) // 2
        guess = primes[half]
        if n == guess:
            return True
        elif half == 0:
            return False
        elif n < guess:
            primes = primes[:half]
        elif n > guess:
            primes = primes[half:]
