from collections import defaultdict
import pytest

from utils.generic_functions import obtain_lines
import os
import time


TEST_CASE = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
TEST_2 = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""
TEST_3 = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""


def get_p1(mat: list[list[str]]) -> int:
    n, m = len(mat), len(mat[0])
    ans = 0

    def explore(i: int, j: int) -> int:
        area = 0
        peri = 0
        stack = [(i, j)]
        store = defaultdict(list)
        c = mat[i][j]
        mat[i][j] = c.lower()

        def handle_store(a, b, dx, dy):
            if (dx, dy) == (1, 0):
                # down
                store[(a, "Down")].append(b)
            elif (dx, dy) == (-1, 0):
                # up
                store[(a, "Up")].append(b)
            elif (dx, dy) == (0, -1):
                # left
                store[(b, "left")].append(a)

            elif (dx, dy) == (0, 1):
                # right
                store[(b, "right")].append(a)

        while stack:
            a, b = stack.pop()
            mat[a][b] = mat[a][b].lower()
            area += 1
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                x, y = a + dx, b + dy

                if n > x >= 0 <= y < m:
                    if mat[x][y] == c:
                        stack.append((x, y))
                        mat[x][y] = c.lower()
                    if mat[x][y].lower() != c.lower():
                        peri += 1
                        handle_store(a, b, dx, dy)

                else:
                    peri += 1
                    handle_store(a, b, dx, dy)

        def get_sides():
            ans = 0
            for l in store.values():
                l.sort()
                ans += 1
                for i in range(1, len(l)):
                    if l[i] != l[i - 1] + 1:
                        ans += 1
            return ans

        return area * get_sides()

    for i in range(n):
        for j in range(m):
            if mat[i][j].isupper():
                ans += explore(i, j)
    return ans


@pytest.mark.parametrize(
    "input, output",
    [
        ([list(row) for row in TEST_CASE.splitlines() if row], 1206),
        ([list(row) for row in TEST_2.splitlines() if row], 436),
        ([list(row) for row in TEST_3.splitlines() if row], 368),
        ([list(row) for row in obtain_lines()], 885394),
    ],
)
def test_p1_d12_y24(input, output):
    assert get_p1(input) == output


# get_p1([list(row) for row in TEST_2.splitlines() if row] )
