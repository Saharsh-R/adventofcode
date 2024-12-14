"""

a, b         x1, y1        x2, y2         c, d      m, n    p, q

x1 = a + x2/ 2 => a = 2 * x1 - x2
y1 = b + y2 / 2 => b = 2 * y1 - y2

x1 = x2 + 2 m / 3
m = 3 * x1 - x2 / 2
n = 3 y1 - y2 / 2

x2 = (x1 + 3 * p) / 4
x1 =( 4 x2 - x1 ) / 3

c = 2 * x2 - x1
d = 2 * y2 - y1

m = 3 * x2 - x1
n = 3 * y2 - y1

p = 4 * x2 - x1
q = 4 * y2 - y1

.B..
.A..
....
C..C

"""

from itertools import combinations
from collections import defaultdict

from utils.generic_functions import obtain_lines


TEST_CASE = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............",
]


def get_unique(mat: list[str]):
    n, m = len(mat), len(mat[0])
    store = defaultdict(list)
    for i, row in enumerate(mat):
        for j, c in enumerate(row):
            if c != ".":
                store[c].append((i, j))
    nodes = set()
    for c in store:
        for combi in combinations(store[c], 2):
            (x1, y1), (x2, y2) = combi

            c = 2 * x2 - x1
            d = 2 * y2 - y1

            a = 2 * x1 - x2
            b = 2 * y1 - y2
            if n > a >= 0 <= b < m:
                nodes.add((a, b))
            if n > c >= 0 <= d < m:
                nodes.add((c, d))
    print(nodes)
    return len(nodes)


def test_d7_24_p1():
    assert get_unique(obtain_lines()) == 398


def get_unique_p2(mat: list[str]):
    n, m = len(mat), len(mat[0])
    store: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)
    for i, row in enumerate(mat):
        for j, c in enumerate(row):
            if c != ".":
                store[c].append((i, j))
    nodes: set[tuple[int, int]] = set()

    def expand(x1, y1, x2, y2) -> set[tuple[int, int]]:
        ans = set()
        dx = x2 - x1
        dy = y2 - y1
        r = 1
        """
        a  x1  x2
          x1 - d   d
        """
        ans.add((x1, y1))
        while True:
            a = x1 - r * dx
            b = y1 - r * dy
            print(a, b, r, x1, y1, x2, y2)
            if n > a >= 0 <= b < m:
                ans.add((a, b))
                r += 1
            else:
                break
        return ans

    for c in store:
        for combi in combinations(store[c], 2):
            (x1, y1), (x2, y2) = combi
            nodes |= expand(x1, y1, x2, y2)
            nodes |= expand(x2, y2, x1, y1)

    return len(nodes)


def test_d7_24_p2():
    assert get_unique_p2(TEST_CASE) == 34
    assert get_unique_p2(obtain_lines()) == 1333
