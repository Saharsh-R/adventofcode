import pytest

from functools import cache

from utils.generic_functions import obtain_lines


@cache
def get_next(n: int) -> list[int]:
    if n == 0:
        return [1]
    sn = str(n)
    if len(sn) % 2 == 0:
        half = len(sn) // 2
        return [int(sn[:half]), int(sn[half:])]
    else:
        return [n * 2024]


@pytest.mark.parametrize("input, output", [(125, [253000]), (0, [1]), (1000, [10, 0])])
def test_get_nex(input, output):
    assert get_next(input) == output


def get_blink(input: list[int]) -> int:
    return sum(get_number(x, 75) for x in input)


def expand(input: list[int]) -> list[int]:
    ans = []
    for x in input:
        ans.extend(get_next(x))
    return ans


def expand_times(input: list[int], n: int):
    curr = input
    for _ in range(n):
        print(_)
        curr = expand(curr)
    return curr


@pytest.mark.parametrize(
    "input, output",
    [([125, 17], 55312), ([int(x) for x in obtain_lines()[0].split()], 0)],
)
def test_d11_y24_p1(input, output):
    assert get_blink(input) == output


@cache
def get_number(x: int, times: int) -> int:
    if times == 1:
        return len(get_next(x))
    return sum(get_number(y, times - 1) for y in get_next(x))
