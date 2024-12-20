# Day 15, Year 2024
# put example test cases here in 1.txt in the same folder
# by default is input.txt

from collections import deque
import os
import time
import pytest

from utils.generic_functions import obtain_lines

def extract_mat_and_directions(day_input: list[str]):
    mat = []
    zoo = deque(day_input)
    while zoo:
        s = zoo.popleft()
        if not s:
            break
        mat.append(list(s))
    directions = deque()
    while zoo:
        s = zoo.popleft()
        for d in s:
            directions.append(d)
    return mat, directions

def get_modified_row(s:str):
    '''
If the tile is #, the new map contains ## instead.
If the tile is O, the new map contains [] instead.
If the tile is ., the new map contains .. instead.
If the tile is @, the new map contains @. instead.
    '''
    ans = []
    for c in s:
        if c == '#':
            ans.append('#')
            ans.append('#')
        elif c == 'O':
            ans.append('[')
            ans.append(']')
        elif c == '.':
            ans.append('.')
            ans.append('.')
        elif c == '@':
            ans.append('@')
            ans.append('.')
        else:
            assert False
    return ans

def extract_mat_and_directions_part_2(day_input: list[str]):
    mat = []
    zoo = deque(day_input)
    while zoo:
        s = zoo.popleft()
        if not s:
            break
        mat.append(get_modified_row(s))
    directions = deque()
    while zoo:
        s = zoo.popleft()
        for d in s:
            directions.append(d)
    return mat, directions



def find_robot_pos(mat):
    n, m = len(mat), len(mat[0])
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '@':
                return i, j

def move_direction(a, b, dx, dy,mat):
    n, m = len(mat), len(mat[0])
    ta, tb = a, b
    while n > ta >= 0 <= tb < m and mat[ta][tb] in ('@', 'O', '[', ']'):
        ta, tb = ta + dx, tb + dy
    edge_a, edge_b = ta , tb
    ta -= dx
    tb -= dy
    if mat[edge_a][edge_b] == '#':
        return
    while (edge_a, edge_b) != (a, b):
        mat[ta][tb], mat[edge_a][edge_b] = mat[edge_a][edge_b], mat[ta][tb]
        edge_a -= dx
        ta -= dx
        edge_b -= dy
        tb -= dy


def can_move(a,b, dx, dy, mat):
    n, m= len(mat), len(mat[0])
    stack = []
    validated = set()
    validated.add((a, b))
    stack.append((a + dx, b + dy))
    validated.add((a + dx, b + dy))
    while stack:
        a, b = stack.pop()
        if mat[a][b] == '[':
            if (a, b+1 ) not in validated:
                stack.append((a, b + 1))
                validated.add((a, b + 1))
        else:
            if (a, b - 1) not in validated:
                stack.append((a, b - 1))
                validated.add((a, b- 1))
        if mat[a + dx][b + dy ] == '#':
            return False
        elif mat[a + dx][b + dy] in ('[',']') and (a + dx,  b + dy) not in validated:
            stack.append((a + dx, b + dy))
            validated.add((a + dx, b + dy))
    return validated

def move_direction_part2(a, b, dx, dy,mat):
    n, m = len(mat), len(mat[0])
    aa, bb = a + dx, b + dy
    if mat[aa][bb] == '.':
        mat[aa][bb] = '@'
        mat[a][b] = '.'
        return
    if mat[aa][bb] == '#':
        return
    if dx == 0:
        move_direction(a,b,dx,dy,mat)
        return
    zoo = can_move(a,b,dx,dy, mat)

    if not zoo:
        return

    #TODO start moving blocks
    for a, b in sorted(zoo,reverse=(dx == 1)):
        aa, bb = a + dx, b + dy
        mat[a][b], mat[aa  ][bb] = mat[aa][bb], mat[a][b]





def move_robot(mat, d ):

    a,b  = find_robot_pos(mat)
    if d == '<':
        move_direction_part2(a,b, 0, -1,mat)
    elif d == '>':
        move_direction_part2(a,b, 0, 1,mat)
    elif d == '^':
        move_direction_part2(a,b, -1, 0,mat)
    elif d == 'v':
        move_direction_part2(a,b, 1, 0,mat)
    else:
        assert False



def get_value(mat):
    ans =0
    n, m = len(mat), len(mat[0])
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 'O':
                ans += 100 * i + j
    return ans

def get_value_part_2(mat):
    ans =0
    n, m = len(mat), len(mat[0])
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '[':
                ans += 100 * i + j
    return ans
DEBUG = True
DEBUG_TIMER = 0.001

def debug_mat(mat,d):
    if not DEBUG:
        return
    print(d)
    print()
    for row in mat:
        print(''.join(row))
    time.sleep(DEBUG_TIMER)
    os.system('clear')


def get_p1(day_input: list[str]):
    mat, directions = extract_mat_and_directions(day_input)
    debug_mat( mat, 'start')
    for d in directions:
        debug_mat( mat, d)
        move_robot(mat, d)

    return get_value(mat)



@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 10092),
    (obtain_lines('2'), 2028),
    (obtain_lines(), 1437174),
])
def test_d15_y2024_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

def get_p2(day_input: list[str]):
    mat, directions = extract_mat_and_directions_part_2(day_input)
    for d in directions:
        debug_mat(mat, d)
        move_robot(mat, d)

    debug_mat(mat, 'final value')
    return get_value_part_2(mat)

@pytest.mark.parametrize('day_input, output', [
    # (obtain_lines('1'), 9021),
    # (obtain_lines('3'), 9021),
    (obtain_lines(), 222),
])
def test_d15_y2024_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

