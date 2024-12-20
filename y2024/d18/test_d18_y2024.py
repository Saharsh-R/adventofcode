# Day 18, Year 2024
# put example test cases here in 1.txt in the same folder
# by default is input.txt

from collections import defaultdict
from enum import StrEnum
import heapq
import re
from math import inf
import pytest

from utils.generic_functions import obtain_lines

n, m = 71, 71
def exit_mat(mat: list[tuple[int]]) -> int:
    mat = set(mat)
    dist = defaultdict(lambda: inf)
    dist[0, 0] = 0
    q = [(0, 0, 0)]
    while q:
        d, a, b = heapq.heappop(q)
        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            x, y = a + dx, b + dy
            if n > x >= 0 <= y < m and (x, y) not in mat and dist[a, b] + 1 < dist[x, y]:
                dist[x, y] = 1 + dist[a, b]
                heapq.heappush(q, (d + 1, x, y))

    return dist[(70, 70)]

def get_int(s: str) -> list[int]:
    matches = re.findall(r"\d+", s)
    return [int(match) for match in matches]


def get_p1(day_input: list[str]):
    mat = []
    for s in day_input[:1024]:
        mat.append(tuple(get_int(s)))
    return exit_mat(mat)




@pytest.mark.parametrize('day_input, output', [
    # (obtain_lines('1'), 1),
    (obtain_lines(), 248),
])
def test_d18_y2024_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

class Edges(StrEnum):
    TOP = "TOP"
    BOTTOM = "BOTTOM"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

class UnionFind:
    def __init__(self):
        self.f = {}

    def find(self, x):
        self.f.setdefault(x, x)
        if x != self.f[x]:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.f[y] = x
            return True
        return False




def get_p2(day_input: list[str]):
    u = UnionFind()
    mat = set()
    def can_exit():
        if u.find(Edges.TOP) == u.find(Edges.BOTTOM):
            return False
        if u.find(Edges.LEFT) == u.find(Edges.RIGHT):
            return False
        if u.find(Edges.TOP) == u.find(Edges.LEFT):
            return False
        if u.find(Edges.BOTTOM) == u.find(Edges.RIGHT):
            return False
        return True

    for i, s in enumerate(day_input):
        l = tuple(get_int(s))
        x, y = l
        if x == 0:
            u.union(l, Edges.TOP)
        if x == n - 1:
            u.union(l, Edges.BOTTOM)
        if y == 0:
            u.union(l, Edges.LEFT)
        if y == n - 1:
            u.union(l, Edges.RIGHT)
        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            a, b = x + dx, y + dy
            if (a, b) in mat:
                u.union((a, b), l)
        mat.add(l)
        if not can_exit():
            return f'{x},{y}'
    assert False, 'no obstacle detected'

@pytest.mark.parametrize('day_input, output', [
    # (obtain_lines('1'), 2),
    (obtain_lines(), 222),
])
def test_d18_y2024_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

