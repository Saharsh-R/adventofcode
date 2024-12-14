import pytest

from utils.generic_functions import obtain_lines


TEST_CASE = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def parse_input(input: str) -> tuple[int, list[int]]:
    a, b = input.split(":")
    return int(a), list(map(int, b[1:].split(" ")))


PARSED_TEST = [parse_input(s.strip()) for s in TEST_CASE.split("\n") if s]


def can_happen_p1(value: int, digits: list[int]) -> bool:
    n = len(digits)

    def back(curr: int, i: int) -> bool:
        if i == n:
            return curr == value
        x = digits[i]
        return back(curr + x, i + 1) or back(curr * x, i + 1)

    return back(digits[0], 1)


def can_happen(value: int, digits: list[int]) -> bool:
    n = len(digits)

    def back(curr: int, i: int) -> bool:
        if i == n:
            return curr == value
        x = digits[i]
        combined = int(str(curr) + str(x))
        return back(curr + x, i + 1) or back(curr * x, i + 1) or back(combined, i + 1)

    return back(digits[0], 1)


@pytest.mark.parametrize(
    "a,b,output",
    [
        (190, [10, 19], True),
        (3267, [81, 40, 27], True),
        (83, [17, 5], False),
        (156, [15, 6], False),
        (7290, [6, 8, 6, 15], False),
        (161011, [16, 10, 13], False),
        (192, [17, 8, 14], False),
        (21037, [9, 7, 18, 13], False),
        (292, [11, 6, 16, 20], True),
    ],
)
def test_can_happen(a, b, output):
    assert can_happen_p1(a, b) == output


@pytest.mark.parametrize(
    "a,b,output",
    [
        (190, [10, 19], True),
        (3267, [81, 40, 27], True),
        (83, [17, 5], False),
        (156, [15, 6], True),
        (7290, [6, 8, 6, 15], True),
        (161011, [16, 10, 13], False),
        (192, [17, 8, 14], True),
        (21037, [9, 7, 18, 13], False),
        (292, [11, 6, 16, 20], True),
    ],
)
def test_can_happen(a, b, output):
    assert can_happen(a, b) == output


@pytest.mark.parametrize(
    "input, output",
    [(PARSED_TEST, 11387), ([parse_input(s) for s in obtain_lines()], 95297119227552)],
)
def test_p1_d7_24(input, output):
    ans = 0
    for a, b in input:
        if can_happen(a, b):
            ans += a
    assert ans == output
