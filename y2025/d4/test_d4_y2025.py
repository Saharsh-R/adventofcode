# Day 4, Year 2025
# put example test cases here in 1.txt in the same folder
# by default is input.txt

import pytest

from utils.generic_functions import obtain_lines


def get_p1(mat_s):
    return 1
def get_p2(mat_s: list[str]):
    mat = [list(s) for s in mat_s]
    n = len(mat)
    m = len(mat[0])
    ans = 0
    def is_good(i, j):
        if mat[i][j] != '@': 
            return 0
        adj = 0
        for di in (-1,0,1):
            for dj in (-1,0,1):
                if di or dj:
                    if n > di + i >= 0 <= dj + j < m:
                        if mat[i + di][j + dj] == "@":
                            adj += 1
        if adj < 4: 
            mat[i][j] = 'x'
            return 1
        return 0

    ans = 0
    while True:
        boo = sum(is_good(i, j) for i in range(n) for j in range(m))
        if not boo:
            break
        ans += boo
    return ans



@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 13),
    (obtain_lines(), 1569),
])
def test_d4_y2025_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

# def get_p2(day_input: list[str]):
#     return 222

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 43),
    (obtain_lines(), 222),
])
def test_d4_y2025_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

                                
