# Day 20, Year 2024
# put example test cases here in 1.txt in the same folder
# by default is input.txt

from collections import Counter, defaultdict
from heapq import heappop, heappush
from math import inf
from pyparsing import deque
import pytest

from utils.generic_functions import obtain_lines


def extract_mat(day_input):
    return [list(s) for s in day_input]

def find_pos(c, mat):
    n, m = len(mat), len(mat[0])
    for i in range(n):
        for j in range(m):
            if mat[i][j] == c:
                return (i, j)
    assert False, f"{c} not found in mat"

def get_dist(mat, a, b):
    n, m = len(mat), len(mat[0])
    dist = defaultdict(lambda: inf)

    q = [(0,a,b)]
    dist[a,b] = 0
    while q:
        d, x, y = heappop(q)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            a, b = dx + x, dy + y
            if n > a >= 0 <= b < m and mat[a][b] != '#' and dist[a, b] > d + 1:
                dist[a, b] = d + 1
                heappush(q, (d + 1, a, b))
    return dist

def get_p1(day_input: list[str]):
    mat = extract_mat(day_input)
    start_x, start_y = find_pos('S', mat)
    end_x, end_y = find_pos('E', mat)
    start_dist = get_dist(mat, start_x, start_y)
    end_dist = get_dist(mat, end_x, end_y)
    # return get_cheats(mat, start_dist, end_dist)
    return get_cheats_big(mat, start_dist, end_dist, 2)

def get_cheats(mat, start_dist, end_dist):
    n, m = len(mat), len(mat[0])
    sx, sy = find_pos('S', mat)
    ex, ey = find_pos('E', mat)
    l = []
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if mat[i][j] == '#':
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if mat[i + dx][j + dy] != '#' and mat[i - dx][j - dy] != '#':
                        saved_time = start_dist[ex, ey] - start_dist[i + dx, j + dy] - end_dist[i - dx, j - dy] - 2
                        if saved_time >= 100:
                            l.append(saved_time)
    return len(l)

def get_cheats_big(mat, start_dist, end_dist, seconds):
    n, m = len(mat), len(mat[0])
    def get_neighbour(i, j):
        q = deque()
        q.append((0, i, j))
        visited = {(i, j)}
        ans = []
        while q:
            s, a, b = q.popleft()
            if mat[a][b] != '#':
                ans.append((s, a,b ))
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x, y = dx + a, b + dy
                if n > x >= 0 <= y < m and (x, y) not in visited and s + 1 <= seconds:
                    q.append((s + 1, x, y))
                    visited.add((x, y))
        return ans

    sx, sy = find_pos('S', mat)
    ex, ey = find_pos('E', mat)
    l = []
    for i in range( n ):
        for j in range(m):
            if mat[i][j] != '#':
                for s,a, b in get_neighbour(i, j):
                    saved_time = start_dist[ex, ey] - start_dist[i , j] - end_dist[a,b] - s
                    if saved_time > 0:
                        l.append(saved_time)
    l.sort()
    z = Counter(l)
    print(z)
    for a in z:
        print('----', a, 'seconds saved -->',z[a], ' times' )
    return sum(x>= 100 for x in l)






@pytest.mark.parametrize('day_input, output', [
    # (obtain_lines('1'), 1),
    (obtain_lines(), 1429),
])
def test_d20_y2024_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

def get_p2(day_input: list[str]):
    mat = extract_mat(day_input)
    start_x, start_y = find_pos('S', mat)
    end_x, end_y = find_pos('E', mat)
    start_dist = get_dist(mat, start_x, start_y)
    end_dist = get_dist(mat, end_x, end_y)
    return get_cheats_big(mat, start_dist, end_dist, 20)

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 2),
    (obtain_lines(), 222),
])
def test_d20_y2024_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

