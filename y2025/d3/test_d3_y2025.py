# Day 3, Year 2025
# put example test cases here in 1.txt in the same folder
# by default is input.txt

import pytest

from utils.generic_functions import obtain_lines

def get_largest(s:str)-> int:
    n = len(s)
    answer =0
    for i in range(n):
        for j in range(i+1, n):
            answer =max(answer, int(s[i] + s[j]))
    return answer

from functools import cache
from math import inf
def get_big(s: str, digits: int) -> int:
    n = len(s)
    @cache
    def dp(i, j):
        if j == 0:
            return 0
        if i == -1:
            return -inf 
        ans = dp(i - 1, j) 
        ans = max(ans, dp(i-1, j -1) * 10 + int(s[i]) )
        return ans
            


        

    return dp(n - 1, 12)
    

def get_p1(day_input: list[str]):
    return sum(get_big(s, 2) for s in day_input)


@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 357),
    (obtain_lines(), 17432),
])
def test_d3_y2025_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

def get_p2(day_input: list[str]):
    return sum(get_big(s, 12) for s in day_input)

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 3121910778619),
    (obtain_lines(), 173065202451341),
])
def test_d3_y2025_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

                                