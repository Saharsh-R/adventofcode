# Day 2, Year 2025
# put example test cases here in 1.txt in the same folder
# by default is input.txt

import pytest

from utils.generic_functions import obtain_lines
from .s_list import zoo


def isinvalid(n: int) -> bool:
    s = str(n)
    if len(s) % 2:
        return False
    half = len(s) // 2
    a, b = s[:half], s[half:]
    return a == b


@pytest.mark.parametrize(
    "n, result", [(11, True), (22, True), (244, False), (1188511885, True)]
)
def test_isinvalid(n, result):
    assert isinvalid(n) == result


def get_double(x: int) -> int:
    a = str(x)
    return int(a + a)


def get_invalid_numbers_between(aa: int, bb: int) -> list[int]:
    a = str(aa)
    b = str(bb)

    start = int(a[: len(a) // 2] or 0)
    end = int(b[: (len(b) + 1) // 2])
    answer = []
    for x in range(start, end + 1):
        y = get_double(x)
        if aa <= y <= bb:
            answer.append(y)
    return answer


import bisect


def get_invalid_numbers_p2(a: int, b: int) -> list[int]:
    i = bisect.bisect_left(zoo, a)
    j = bisect.bisect_right(zoo, b)
    return zoo[i:j]


def test_ad():
    a = "2342"
    b = a[:0]


@pytest.mark.parametrize(
    "a,b,numbers",
    [
        (1, 22, [11, 22]),
        (1, 100, [11, 22, 33, 44, 55, 66, 77, 88, 99]),
        (95, 115, [99]),
        (998, 1012, [1010]),
        (1188511880, 1188511890, [1188511885]),
        (222220, 222224, [222222]),
        (38593856, 38593862, [38593859]),
        (1698522, 1698528, []),
        (446443, 446449, [446446]),
        (2121212118, 2121212124, []),
    ],
)
def test_get_invalid(a, b, numbers):
    assert get_invalid_numbers_between(a, b) == numbers


@pytest.mark.parametrize(
    "a,b,numbers",
    [
        (11, 22, [11, 22]),
        (95, 115, [99, 111]),
        (998, 1012, [999, 1010]),
        (1188511880, 1188511890, [1188511885]),
        (222220, 222224, [222222]),
        (1698522, 1698528, []),
        (446443, 446449, [446446]),
        (38593856, 38593862, [38593859]),
        (565653, 565659, [565656]),
        (824824821, 824824827, [824824824]),
        (2121212118, 2121212124, [2121212121]),
    ],
)
def test_get_invalid_p2(a, b, numbers):
    assert get_invalid_numbers_p2(a, b) == numbers


def get_p1(day_input: list[str]):
    full_list = day_input[0].split(",")

    anser = 0
    for n_range in full_list:
        numbers = n_range.split("-")
        aux_sum = sum(get_invalid_numbers_between(int(numbers[0]), int(numbers[1])))
        anser += aux_sum
    return anser


@pytest.mark.parametrize(
    "day_input, output",
    [
        (obtain_lines("1"), 1227775554),
        (obtain_lines(), 111),
    ],
)
def test_d2_y2025_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output


def get_p2(day_input: list[str]):
    full_list = day_input[0].split(",")

    anser = 0
    for n_range in full_list:
        numbers = n_range.split("-")
        aux_sum = sum(get_invalid_numbers_p2(int(numbers[0]), int(numbers[1])))
        anser += aux_sum
    return anser


@pytest.mark.parametrize(
    "day_input, output",
    [
        (obtain_lines("1"), 4174379265),
        (obtain_lines(), 40028128307),
    ],
)
def test_d2_y2025_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output
