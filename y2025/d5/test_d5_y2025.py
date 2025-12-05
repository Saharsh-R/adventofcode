# Day 5, Year 2025
# put example test cases here in 1.txt in the same folder
# by default is input.txt

import pytest

from utils.generic_functions import obtain_lines

from collections import deque

def get_p1(day_input_d: list[str]):
    day_input = deque(day_input_d) 
    store = []
    while day_input[0]:
        words = day_input.popleft().split('-')
        a,b = int(words[0]),int( words[1])
        store.append((a,b))
    assert day_input.popleft() == ''
    ans =0
    while day_input:
        x = int(day_input.popleft())
        if any(a <= x <= b for a, b in store):
            ans += 1
    return ans
    
    
def get_p2(day_input_d: list[str]):
    day_input = deque(day_input_d) 
    store = []
    while day_input[0]:
        words = day_input.popleft().split('-')
        a,b = int(words[0]),int( words[1])
        store.append((a,b))
    assert day_input.popleft() == ''
    store.sort()
    ans =0

    start, end = store[0]
    for a, b in store[1:]:
        if start <= b and a <= end:
            end = max(b, end)
        else:
            ans += end - start + 1
            start, end = a, b
    ans += end - start + 1
    return ans

    


@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 3),
    (obtain_lines(), 111),
])
def test_d5_y2025_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

# def get_p2(day_input: list[str]):
#     return 222

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 14),
    (obtain_lines(), 222),
])
def test_d5_y2025_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

                                