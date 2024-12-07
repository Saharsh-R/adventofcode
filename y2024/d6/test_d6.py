from collections import Counter
import pytest
from utils.generic_functions import obtain_lines
import copy


def test_route():
    l = set()
    for x in obtain_lines():
        l.add(len(x))
    assert l == {130}


def test_str_change():
    s = "dog"
    l = list(s)
    assert l == ["d", "o", "g"]


def paint_mat(mat_ori: list[list[str]]) -> list[list[str]]:
    mat = copy.deepcopy(mat_ori)
    n, m = len(mat), len(mat[0])
    a, b = -1, -1
    store = set()

    def is_in_bound(x: int, y: int) -> bool:
        return n > x >= 0 <= y < m

    for i in range(n):
        for j in range(m):
            if mat[i][j] == "^":
                a, b = i, j
                break
    assert a != -1
    assert b != -1
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    di = 0
    while is_in_bound(a, b):
        mat[a][b] = "X"
        dx, dy = direction[di]
        if (a, b, di) in store:
            return False
        store.add((a, b, di))

        z = 0
        while is_in_bound(a + dx, b + dy) and mat[a + dx][b + dy] == "#":
            di = (di + 1) % 4
            dx, dy = direction[di]
            z += 1
            if z== 5:
                assert False
        a += dx
        b += dy
    return mat, True


def count_x(mat: list[list[str]]) -> int:
    return sum(x == "X" for row in mat for x in row)


ZOO_INPUT = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]


@pytest.mark.parametrize("input, output", [(ZOO_INPUT, 41), (obtain_lines(), 4988)])
def test_d6_24_p1(input, output):
    input = [list(s) for s in input]
    mat, store = paint_mat(input)
    assert count_x(mat) == output


@pytest.mark.parametrize(
    "input, output",
    [
        (ZOO_INPUT, 6),
        (obtain_lines(), 0)
    ],
)
def test_d6_24_p2(input, output):
    input = [list(s) for s in input]
    n, m = len(input), len(input[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if input[i][j] == '.':
                input[i][j] = '#'
                if paint_mat(input) == False:
                    ans += 1
                input[i][j] ='.'
    assert ans == output



