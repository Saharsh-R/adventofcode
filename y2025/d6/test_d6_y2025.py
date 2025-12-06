# Day 6, Year 2025
# put example test cases here in 1.txt in the same folder
# by default is input.txt

import pytest

from utils.generic_functions import obtain_lines


def get_p1(input_d1: list[str]):


    mat = [s.split() for s in input_d1]
    n, m = len(mat), len(mat[0])
    def f_mul(row):
        ans = 1
        for j in range(n - 1):
            ans *= int(mat[j][row])
        return ans

    def f_add(row):
        return sum(int(mat[i][row]) for i in range(n - 1))

    ans = 0
    for row in range(m):
        operation = mat[-1][row]
        if operation == '*':
            ans += f_mul(row)
        else:
            ans += f_add(row)
    return ans



@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 4277556),
    (obtain_lines(), 111),
])
def test_d6_y2025_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

def get_p2(mat: list[str]):
    n, m = len(mat), len(mat[0])
    ans =0
    def get_numbers(i) -> list[int]:
        ans :list[int]= []
        col = i
        while col < m and any(mat[i][col] != ' ' for i in range(n- 1)):
            sub = '' 
            for j in range(0, n - 1):
                sub += mat[j][col]
            ans.append(int(sub))
            col += 1
        return ans

    def f_mul(i):
        ans = 1
        for x in get_numbers(i):
            ans *= x
        return ans

    def f_add(i):
        return sum(get_numbers(i)) 
    for i in range(m):
        c = mat[-1][i]
        if c == ' ':
            continue
        elif c == '*': 
            ans += f_mul(i)
        else:
            ans += f_add(i)
    return ans
        



@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 2),
    (obtain_lines(), 222),
])
def test_d6_y2025_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

                                