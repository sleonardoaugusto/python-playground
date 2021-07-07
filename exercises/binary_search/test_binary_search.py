from exercises.binary_search.binary_search import search


def test_should_return_2_500_000_000_000():
    assert search(n=2_500_000_000_000) == 2_500_000_000_000


def test_should_return_5_000_000_000_000_000():
    assert search(n=5_000_000_000_000_000) == 5_000_000_000_000_000


def test_should_return_7_500_000_000_000():
    assert search(n=7_500_000_000_000) == 7_500_000_000_000


def test_should_return_10_000_000_000_000():
    assert search(n=10_000_000_000_000) == 10_000_000_000_000
