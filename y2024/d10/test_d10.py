from collections import Counter
import pytest

from utils.generic_functions import obtain_lines

TEST_CASE = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


def get_mat(s: str):
    return [[int(x) for x in row] for row in s.splitlines() if row]


def test_mat():
    mat = get_mat(TEST_CASE)
    n, m = len(mat), len(mat[0])
    for row in mat:
        assert len(row) == m


def get_p1(mat: list[list[int]]) -> int:
    peaks = Counter()
    n, m = len(mat), len(mat[0])
    stack = []
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                stack.append((i, j, 0, i, j))
    while stack:
        i, j, curr, xx, yy = stack.pop()
        if curr == 9:
            peaks[(i, j, xx, yy)] += 1
            continue
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            a, b = i + dx, j + dy
            if n > a >= 0 <= b < m and mat[a][b] == curr + 1:
                stack.append((a, b, curr + 1, xx, yy))

    return sum(v for v in peaks.values())


@pytest.mark.parametrize(
    "input,output",
    [
        (get_mat(TEST_CASE), 81),
        ([[int(c) for c in row] for row in obtain_lines()], 0),
    ],
)
def test_d10_24_p1(input: list[list[int]], output: int):
    assert get_p1(input) == output
