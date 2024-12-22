# Day 21, Year 2024
# put example test cases here in 1.txt in the same folder
# by default is input.txt

from functools import cache
from math import inf
import pytest
from itertools import permutations, groupby
from y2024.d21.utils_boo import generate_ways_utils

from utils.generic_functions import obtain_lines

numpad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['', '0', 'A'],
]
keypad = [
    ['', '^', 'A'],
    ['<', 'v', '>'],
]

numeric_keypad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2)
}
direction_keypad = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2)
}

@cache
def get_coord(c, is_numpad):
    mat = numpad if is_numpad else keypad
    n, m = len(mat), len(mat[0])
    for i in range(n):
        for j in range(m):
            if mat[i][j] == c:
                return i, j
    assert False, f"{c} not found in is_numpad: {is_numpad}"


@cache
def generate_ways(a, b , is_numpad):
    # return generate_ways_utils(a, b, is_numpad)


    i, j = get_coord(a, is_numpad)
    x, y = get_coord(b, is_numpad)

    want = '' 
    if i < x:
        want += 'v' * (x - i)
    elif i > x: 
        want += '^' * (i - x)
    if j > y:
        want += '<' * (j - y)
    elif j < y:
        want += '>' * (y - j)
    good_ways = []
    for possible_way in get_unique_permutations(want): 
        if is_valid_path(a,possible_way, is_numpad):
            good_ways.append(possible_way)
    return good_ways


@pytest.mark.parametrize('input, output', [
    [('<', '^', False),(1) ],
    [('<', 'A', False),(2) ],
    [('A', 'v', False),(2) ],
])
def test_generate_ways(input, output):
    assert len(generate_ways(*input)) == output
    
def get_unique_permutations(s):
    return list(set(''.join(p) + "A" for p in permutations(s)))

def is_valid_path(start_c, path, is_numpad):
    a, b = get_coord(start_c, is_numpad)
    zoo = numeric_keypad if is_numpad else direction_keypad
    for c in path:
        if c == '>':
            b += 1
        elif c == '<':
            b -= 1
        elif c == '^':
            a -= 1
        elif c == 'v':
            a += 1
        else:
            assert False
        if (a, b) not in zoo.values() :
            return False
    return True


def test_get_unique_permutations():
    want = ['<<^', '<^<', '^<<']
    got = get_unique_permutations('<<^')
    want.sort()
    got.sort()
    assert want == got 
    
@cache
def get_cost(a, b, depth, is_numpad):
    if depth == 0:
        assert is_numpad
        return min([len(x) for x in generate_ways(a, b, True)])
    ans = inf
    for way in generate_ways(a, b , is_numpad):
        score = 0
        way = 'A' + way
        for x, y in zip(way, way[1:]):
            score += get_cost(x, y, depth - 1, True)
        ans = min(ans, score)

    return ans







def get_p1(day_input: list[str]):
    ans = 0
    for x in day_input:
        row_sum = 0
        x = 'A' + x
        for a, b in zip(x, x[1:]):
            row_sum += get_cost(a, b, 25, False  )
        ans += row_sum * int(x[1:4])
    return ans



@pytest.mark.parametrize('day_input, output', [
    # (obtain_lines('1'), 126384),
    (obtain_lines(), 231564),
])
def test_d21_y2024_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

def get_p2(day_input: list[str]):
    ans = 0
    for x in day_input:
        row_sum = 0
        for a, b in zip(x, x[1:]):
            row_sum += get_cost(a, b, 25, False)
    return ans


@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 2),
    (obtain_lines(), 222),
])
def test_d21_y2024_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

                                