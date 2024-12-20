from collections import defaultdict
def test_set_union():
    a = {1}
    b = {2}
    a |= b
    assert a == {1, 2}

def test_set_add():
    a = {3}
    b = {4, 5 }
    assert a|b == {3, 4, 5}

def test_set_change():
    boo = defaultdict(set)
    boo[1].add(3)
    assert boo[1] == {3}
    boo[1] = {7}
    assert boo[1] == {7}

def test_default():
    boo = defaultdict(set)
    boo[1, 2] = {1}
    assert boo[1, 2] == boo[(1,2)] == {1}
    boo[(1, 2)]  = {2}
    assert boo[1, 2] == boo[(1,2)] == {2}

def test_set_set():
    a = {1}
    a.add((2, 3))
    assert a == {1, (2, 3)}
