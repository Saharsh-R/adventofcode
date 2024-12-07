import pytest
import re
from utils.generic_functions import obtain_lines


PATTERN = r"mul\(\d+,\d+\)"
DO_DONT = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"


def get_matches(s: str) -> list[str]:
    return re.findall(PATTERN, s)


def get_p2_matches(s: str) -> list[str]:
    return re.findall(DO_DONT, s)


TESTING_STRING = "ado()sdmul(923,3)flkdon't()afmul(44,5)"


def test_regex_pattern():
    text = get_matches(TESTING_STRING)
    assert text == ["mul(923,3)", "mul(44,5)"]


def test_p2_regex_pattern():
    text = get_p2_matches(TESTING_STRING)
    assert text == ["do()", "mul(923,3)", "don't()", "mul(44,5)"]


def extract_value(s: str) -> tuple[int, int] | bool:
    if s == "do()":
        return True
    if s == "don't()":
        return False

    l = re.findall(r"\d+", s)
    return (int(l[0]), int(l[1]))


def test_value_extractor():
    assert extract_value("mul(923,3)") == (923, 3)


def regex_extractor(input: str, is_p2: bool = False) -> list[tuple[int, int]]:
    return [extract_value(x) for x in get_p2_matches(input)]


@pytest.mark.parametrize(
    "input, output",
    [
        ("mul(2,4),zzzzmul(89,323)", [(2, 4), (89, 323)]),
        ("do()mul(2,4)", [True, (2, 4)]),
    ],
)
def test_match_regex(input, output):
    assert regex_extractor(input) == output


def test_d3_24_p1():
    ans = 0
    for s in obtain_lines():
        ans += sum(a * b for a, b in regex_extractor(s))
    assert ans == 188741603


def test_d3_24_p2():
    ans = 0
    do = True
    for s in obtain_lines():
        for x in regex_extractor(s):
            if isinstance(x, bool):
                do = x
            else:
                if do:
                    ans += x[0] * x[1]
    assert ans == 67269798
