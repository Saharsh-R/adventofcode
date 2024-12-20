# Day 19, Year 2024
# put example test cases here in 1.txt in the same folder
# by default is input.txt

from functools import cache
import pytest

from utils.generic_functions import obtain_lines

def extract_towels(data: list[str]):
    return data[0].split(', '), data[2:]


def get_p1(day_input: list[str]):
    towels, data = extract_towels(day_input)
    ans = 0

    @cache
    def can_form(pattern:str):
        if not pattern:
            return True
        for t in towels:
            if pattern.startswith(t):
                if can_form(pattern[ len(t):]):
                    return True
        return False

    for x in data:
        if can_form(x ):
            ans += 1
    return ans

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 6),
    (obtain_lines(), 111),
])
def test_d19_y2024_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

def get_p2(day_input: list[str]):
    towels, data = extract_towels(day_input)
    total = 0

    @cache
    def can_form(pattern:str):
        if not pattern:
            return 1
        ans = 0
        for t in towels:
            if pattern.startswith(t):
                ans += can_form(pattern[len(t):])
        return ans

    return sum(can_form(x) for x in data)

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 16),
    (obtain_lines(), 222),
])
def test_d19_y2024_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

