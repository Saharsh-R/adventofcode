from utils.generic_functions import obtain_lines
import pytest
from collections import Counter

@pytest.fixture
def input_file():
    input_file = obtain_lines()
    assert len(input_file) == 1000
    yield input_file

def get_pairs(s: str):
    return [int(x) for x in s.split()]

def test_first_pair(input_file):
    assert get_pairs(input_file[0]) == [35446 ,  18696]

def generate_array(input: list[str])-> tuple[list[int], list[int]]:
    a:list[int] = []
    b:list[int] = []
    for s in input:
        x, y = get_pairs(s)
        a.append(x)
        b.append(y)
    return (a,b)

def test_output(input_file):
    a, b = generate_array(input_file)
    a.sort()
    b.sort()
    ans = 0
    for x, y in zip(a, b):
        ans += abs(x - y)
    assert ans == 2196996


def test_similarity(input_file):
    a, b = generate_array(input_file)
    b = Counter(b)
    ans = 0
    for x in a:
        ans += x * b[x]
    assert ans == 0
