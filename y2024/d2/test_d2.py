import pytest
from utils.generic_functions import obtain_lines

def is_safe(l: list[int]|str) -> bool:
    if isinstance(l, str):
        l = list(map(int, l.split()))
    positive = False
    negative = False
    for a, b in zip(l[::], l[1::]):
        if b == a:
            return False
        elif b > a:
            positive = True
        else:
            negative = True
        if not( 1 <= abs(b - a) <= 3):
            return False
    return positive ^ negative

def is_less_safe(input: str) -> bool:
    if is_safe(input):
        return True
    input = list(map(int, input.split()))

    for i in range(len(input)):
        l = input[:i] + input[i+1:]
        if is_safe(l):
            return True
    return False


    # return any(is_safe(input[:i] + input[i + 1:]) for i in range(len(input)))

@pytest.mark.parametrize(
    "level, safe",
    [
        ["7 6 4 2 1", True],
        ["1 2 7 8 9", False],
        ["9 7 6 2 1", False],
        ["1 3 2 4 5", False],
        ["8 6 4 4 1", False],
        ["1 3 6 7 9", True],
    ],
)
def test_is_safe(level, safe):
    assert is_safe(level) == safe


def test_d3_24():
    ans = 0
    for x in obtain_lines():
        if is_safe(x):
            ans += 1
    assert ans == 663

@pytest.mark.parametrize(
    "level, safe",
    [
        ["7 6 4 2 1", True],
        ["1 2 7 8 9", False],
        ["9 7 6 2 1", False],
        ["1 3 2 4 5", True],
        ["8 6 4 4 1", True],
        ["1 3 6 7 9", True],
    ],
)
def test_is_less_safe(level, safe):
    assert is_less_safe(level) == safe


def test_d3_24_p2():
    ans = 0
    for x in obtain_lines():
        if is_less_safe(x):
            ans += 1
    assert ans == 692
