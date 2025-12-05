# Day 1, Year 2025
# put example test cases here in 1.txt in the same folder
# by default is input.txt

import pytest

from utils.generic_functions import obtain_lines


def get_p1(day_input: list[str]):
    start = 50
    answer = 0
    for line in day_input:
        move = int(line[1:])
        if line[0] == 'L':
            start = (start - move) % 100
        else:
            start = (start + move) % 100
        if start == 0:
            answer += 1
    return answer

def get_p2(day_input: list[str]):
    start = 50
    answer = 0
    for line in day_input:
        move = int(line[1:])
        if line[0] == 'L':
            end = (start - move) 
        else:
            end = (start + move) 
        answer += find_clicks(start, end)
        
        start = end % 100
    return answer

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 3),
    (obtain_lines(), 111),
])
def test_d1_y2025_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output


@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 6),
    (obtain_lines(), 222),
])
def test_d1_y2025_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

'''
 -2  -1 | 0 1 2     99 | 100 101
        | 0 1 2     99 |        
          ^              ^
'''  


def find_clicks(start: int, end: int) -> int:
    assert start != end
    if start % 100 == 0:
        if end < start:
            start -= 1
        if end > start:
            start += 1
    if end % 100 == 0:
        if start < end:
            end += 1
        if end < start:
            end -= 1

    a = start // 100
    b = end // 100
    answer = abs(a - b)
    
   
    return answer

def test_abs():
    assert -100 % 100 == 0

@pytest.mark.parametrize('start, end, result', [
    (50, -100, 2),
    (50, -1, 1),
    (50,0, 1),
    (50, 40, 0),
    (50, 60, 0),
    (50, 100, 1),
    (50, 101, 1),
    (50, 200, 2),
    (50,201, 2),
    #
    (0,-100,1 ),
    (0,-1,0 ),
    (0,1,0 ),
    (0,100,1 ),
])
def test_find_clicks(start, end, result):
    assert find_clicks(start, end) == result
