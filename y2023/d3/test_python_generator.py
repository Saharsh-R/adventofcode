def test_sum():
    a = [1, 2, 3, 4, 5]
    assert sum(x for x in a if x % 2 == 0) == 6
    assert sum(x for x in a if x == 6) == 0
