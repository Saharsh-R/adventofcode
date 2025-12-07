# Day 7, Year 2025
# put example test cases here in 1.txt in the same folder
# by default is input.txt

import pytest

from utils.generic_functions import obtain_lines


from collections import Counter

def get_p2(mat_in: list[str]):
    mat = [list(x) for x in mat_in]
    ans = 0
    n, m= len(mat), len(mat[0])
    start = mat[0].index('S')
    beams = Counter()
    beams[start ] = 1
    for row in mat[1:]:
        new_beams = Counter() 
        for i,x in enumerate(row): 
            if beams[i] > 0: 

                if x == '^': 
                    new_beams[i - 1] += beams[i]
                    new_beams[i + 1] += beams[i]
                else:
                    new_beams[i] += beams[i]
        beams = new_beams
        

    return sum(beams[i] for i in range(m))






@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 21),
    (obtain_lines(), 1543),
])
def test_d7_y2025_p1(day_input: list[str], output: int):
    ...
    # assert get_p1(day_input) == output



@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 40),
    (obtain_lines(), 222),
])
def test_d7_y2025_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

                                