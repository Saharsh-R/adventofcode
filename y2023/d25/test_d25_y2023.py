# Day 25, Year 2023
# put example test cases here in 1.txt in the same folder
# by default is input.txt

from collections import defaultdict
import pytest
from itertools import combinations
from utils.generic_functions import obtain_lines
from rich.progress import track


def extract_input(day_input: list[str]):
    graph = defaultdict(list)
    edges = []
    for row in day_input:
        a, nodes = row.split(': ')
        for b in nodes.split():
            graph[a].append(b)
            graph[b].append(a)
            edges.append((a, b))
    return graph, edges


class UnionFind:
    def __init__(self):
        self.f = {}
        self.size = {}

    def find(self, x):
        self.f.setdefault(x, x)
        if x != self.f[x]:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.f[y] = x
            self.size[x] = self.size.get(x, 1) + self.size.get(y, 1)
            return True
        return False

    def get_size(self, x):
        root = self.find(x)
        return self.size.get(root, 1)

    def sizes_of_all_groups(self):
        all_possi =set([self.find(x) for x in self.f])
        return [self.get_size(x) for x in all_possi]




def get_p1(day_input: list[str]):
    graph, edges = extract_input(day_input)
    n = len(edges)
    hits =0
    ans = 1
    print(n * (n - 1) * (n - 2))
    for g in track(combinations(edges, n - 3), description="Processing combinations..."):
        assert len(list(g)) == n - 3
        u = UnionFind()
        for a, b in g:
            u.union(a, b)
        z = u.sizes_of_all_groups()


        if len(z) != 1:
            hits += 1
            assert len(z) == 2
            ans = z[0] * z[1]
    assert hits == 1
    return ans






@pytest.mark.parametrize('day_input, output', [
    # (obtain_lines('1'), 54),
    (obtain_lines(), 111),
])
def test_d25_y2023_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

def get_p2(day_input: list[str]):
    return 222

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 2),
    (obtain_lines(), 222),
])
def test_d25_y2023_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

