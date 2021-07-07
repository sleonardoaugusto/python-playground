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
