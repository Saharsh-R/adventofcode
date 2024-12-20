# Day 16, Year 2024
# put example test cases here in 1.txt in the same folder
# by default is input.txt

from collections import defaultdict
from copy import deepcopy
import heapq
from math import inf
import pytest

from utils.generic_functions import obtain_lines


def make_matrix(data:  list[str]):
    mat:list[list[str]] = []
    for row in data:
        mat.append(list(row))
    return mat

def find_pos_in_mat(mat:list[list[str]], c:str)->tuple[int, int]:
    n, m = len(mat), len(mat[0])
    for i in range(n):
        for j in range(m):
            if mat[i][j] == c:
                return i, j
    assert False, 'no postion found'


def get_p1_score(mat: list[list[str]]):
    return get_p_data(mat)[0]

def debug(mat, path, mind):
    print()
    mat_copy = deepcopy(mat)
    x, y = find_pos_in_mat(mat, 'E')
    for (a,b )in path[(x, y, mind)]:
        mat[a][b] = 'O'
    for row in mat:
        print(''.join(row))
    print()

def get_p_data(mat: list[list[str]]):
    n, m = len(mat), len(mat[0])
    a, b = find_pos_in_mat(mat,'S')
    dist: defaultdict[tuple, float] = defaultdict(lambda: inf)
    path = defaultdict(set)

    q = [] # score, x, y, direction
    q.append((0, a, b, '>'))
    dist[(a, b, '>')] = 0
    path[(a, b, '>')].add((a,b))

    def is_in_bound(x, y):
        return n > x >= 0 <= y < m

    while q:
        score, x, y, direction = heapq.heappop(q)
        if direction == '>':
            nx, ny = x, y + 1
            newd = ['^', 'v']
        elif direction == '<':
            nx, ny = x, y - 1
            newd = ['^', 'v']
        elif direction == '^':
            nx, ny = x - 1, y
            newd = ['>', '<']
        elif direction == 'v':
            nx, ny = x + 1, y
            newd = ['>', '<']
        else:
            assert False, 'check for direction typos'

        if is_in_bound(nx, ny) and mat[nx][ny] != '#'  :
            if  dist[(nx, ny, direction)] > score + 1:
                dist[(nx, ny, direction)] = score + 1
                heapq.heappush(q, (score + 1, nx, ny, direction))
                path[(nx, ny, direction)] = path[(x, y, direction)] | {(nx, ny)}
            elif  dist[(nx, ny, direction)] == score + 1:
                path[(nx, ny, direction)] |= path[(x, y, direction)]
        for nd in newd:
            if dist[(x, y, nd)] > score + 1000:
                dist[(x, y, nd)] = score + 1000
                heapq.heappush(q, (score + 1000, x,y, nd))
                path[x,y, nd] = path[x, y, direction] | {(x, y)}
            elif dist[(x, y, nd)] == score + 1000:
                path[x,y, nd] |= path[x, y, direction]
    xx, yy = find_pos_in_mat(mat,'E')

    minans = inf
    mind = ''
    for d in['^', '<', '>', 'v']:
        if dist[xx, yy, d] < minans:
            minans = dist[xx, yy, d]
            mind = d
    debug(mat, path, mind)
    return minans, len(path[xx, yy,mind ])




    # return min(dist[xx, yy, d] for d in ), len(path[(xx, yy)])



def get_p1(day_input: list[str]):
    mat = make_matrix(day_input)
    return get_p1_score(mat)



@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 7036),
    (obtain_lines('2'), 11048),
    (obtain_lines(), 103512),
])
def test_d16_y2024_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

def get_p2(day_input: list[str]):
    mat = make_matrix(day_input)
    return get_p_data(mat)[1]

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 45),
    (obtain_lines('2'), 64),
    (obtain_lines(), 554),
])
def test_d16_y2024_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

