import re
import pytest
import os
from utils.generic_functions import obtain_lines
import time


def get_numbers(s: str) -> list[int]:
    matches = re.findall(r"-?\d+", s)
    return [int(match) for match in matches]


@pytest.mark.parametrize(
    "input, output",
    [
        ("p=29,54 v=74,-59", [29, 54, 74, -59]),
    ],
)
def test_get_numbers(input, output):
    assert get_numbers(input) == output


def extract_data():
    return [get_numbers(x) for x in obtain_lines()]


def test_extract_data():
    assert extract_data() == []


# WIDTH = 11
# HEIGHT = 7


WIDTH = 101
HEIGHT = 103


def get_posi(x: int, y: int, vx: int, vy: int, n: int) -> tuple[int, int]:
    return (x + n * vx) % WIDTH, (y + n * vy) % HEIGHT


debug_mat = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]


def get_quad(x: int, y: int):
    """
    1   2

    3   4
    """
    debug_mat[y][x] += 1
    half_widht = (WIDTH - 1) // 2
    half_height = (HEIGHT - 1) // 2
    mid_x = half_widht
    mid_y = half_height
    if x == mid_x:
        return 0
    if y == mid_y:
        return 0
    left = x < mid_x
    top = y < mid_y

    if left and top:
        return 1
    elif left:
        return 3
    elif top:
        return 2
    else:
        return 4


def get_quad_count(n: int):
    data = extract_data()
    zoo = [0, 0, 0, 0]
    for x, y, vx, vy in data:
        a, b = get_posi(x, y, vx, vy, n)
        quad = get_quad(a, b)
        if quad:
            zoo[quad - 1] += 1
    return zoo


def get_p1():
    zoo = get_quad_count(100)
    ans = 1
    for x in zoo:
        ans *= x
    return ans


def test_p1_24_d14():
    ans = get_p1()
    assert ans == 1


def print_mat(n: int):
    get_quad_count(n)
    print()
    for x in debug_mat:
        print("".join(["*" if y else " " for y in x]))


def encode_mat():
    return tuple(tuple(row) for row in debug_mat)


def debug_zoo_foo():
    cache = set()
    for i in range(8170, 8180):
        get_quad_count(i)
        print_mat(i)
        print(i)
        print()
        x = encode_mat()
        if x in cache:
            print("zooooooooo")
            break
        cache.add(x)
        time.sleep(0.9)
        for i in range(len(debug_mat)):
            for j in range(len(debug_mat[0])):
                debug_mat[i][j] = 0
        os.system("clear")
