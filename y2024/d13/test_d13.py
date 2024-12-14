from math import inf
import re

import pytest
from utils.generic_functions import obtain_lines


def get_int(s: str) -> tuple[int, int]:
    matches = re.findall(r'\d+', s)
    return [int(match) for match in matches]



@pytest.mark.parametrize('input, output', [
    ("Button A: X+62, Y+35", [62, 35] ),
    ("Button B: X+11, Y+34", [11, 34]),
    ("Prize: X=19628, Y=9357", [19628, 9357]),
])
def test_get_int(input, output):
    assert get_int(input) == output

def extract_stuff():
    data = obtain_lines()
    ans = []
    row = []
    for line in data:
        if not line:
            ans.append(row)
            row = []
        row.extend(get_int(line))
    if row:
        ans.append(row)
    return ans

def test_extract():
    assert len(extract_stuff()) == 320


def find_min_reach(machine) -> int:
    xa, ya, xb, yb, x, y = machine
    ans = inf
    times  = 0
    for a in range(1, 101):
        for b in range(1, 101):
            if xa * a + xb * b != x:
                continue
            if ya * a + yb * b != y:
                continue
            times += 1
            print(a,b)

            ans = min(ans, 3 * a + b)
    assert times <= 1
    return ans

def can_divide(a, b):
    return a % b == 0

LONG = 10000000000000
def find_long_match(machine) -> int:
    '''
    xa * a + xb * b = x
    ya * a + yb * b = y

    a = (x - (b * xb)) / xa
    a = (y - (b * yb)) / ya
    ya * x - ya (b * xb) = xa * y - xa * ( b * yb)

    ya * x - xa * y / ( xb * ya -yb * xa ) = b

    xa * a * yb - x * yb    = ya * a * xb - y  * xb
    a =  x * yb - y * xb / (xa * yb - ya * xb)

    3 * a + b minimize
    '''
    xa, ya, xb, yb, x, y = machine
    x += LONG
    y += LONG
    if not can_divide(ya * x - xa * y,xb * ya -yb * xa ):
        return inf
    if not can_divide((x * yb - y * xb), (xa * yb - ya * xb)):
        return inf

    b = (ya * x - xa * y) / ( xb * ya -yb * xa )
    a =  (x * yb - y * xb) /(xa * yb - ya * xb)


    return 3 * a + b


def get_p1():
    ans = 0
    for row in extract_stuff():
        x = find_min_reach(row)
        if x != inf:
            ans += x
    return ans
def get_p2():
    ans = 0
    for row in extract_stuff():
        x = find_long_match(row)
        if x != inf:
            ans += x
    return ans


def test_d13_24_p1():
    assert get_p1() == 39748

def test_d13_24_p2():
    assert get_p2() == 74478585072604
