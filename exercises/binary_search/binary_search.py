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
    _min_index = 0
    _max_index = len(primes) - 1
    while True:
        half = (_min_index + _max_index) // 2
        guess = primes[half]
        if n == guess:
            return True
        elif half == 0:
            return False
        elif n < guess:
            _max_index = half - 1
        elif n > guess:
            _min_index = half + 1


primes = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]
