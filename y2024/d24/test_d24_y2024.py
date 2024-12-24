# Day 24, Year 2024
# put example test cases here in 1.txt in the same folder
# by default is input.txt
from math import inf
import pytest
from itertools import combinations, permutations
from utils.generic_functions import obtain_lines
import copy


from collections import deque
def extract_data(day_input: list[str]):
    store = {} 
    wires = []
    q = deque(day_input)
    while q:
        x = q.popleft()
        if not x:
            break
        a,b = x.split(': ')
        store[a] = (True, int(b ))
    
    
    while q:
        l = q.popleft().split()
        
        a = l[0]
        command = l[1]
        b = l[2]
        c = l[-1]
        store[c] = (False, (a, command, b))
        wires.append((a, command, b, c))
    return store, wires



def get_number_value(data, c):
    ans_keep = []
    for x in data:
        if x[0] == c:
            ans_keep.append(x)
            if data[x][1] == inf:
                return inf
    ans_keep.sort(reverse=True)
    ans = 0
    for x in ans_keep:
        ans = ans << 1
        ans += data[x][1] 
    return ans



def get_value(data):

    def f(x):
        done, value = data[x]
        if done:
            return value
        a, command, b = value
        a = f(a )
        b = f(b)
        if a == inf or b == inf:
            data[x] = (True, inf)
            return inf
        match command:
            case 'AND':
                data[x] = (True, f(a) & f(b))
            case 'OR':
                data[x] = (True, f(a) | f(b))
            case 'XOR':
                data[x] = (True, f(a) ^ f(b))
        assert data[x][0]
        return data[x][1]

    for x in data:
        f(x)
    return get_number_value(data, 'z')

def get_p1(day_input: list[str]):
    data, _ = extract_data(day_input)
    return get_value(data)

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 2024),
    (obtain_lines('2'), 4),
    (obtain_lines(), 56939028423824),
])
def test_d24_y2024_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

def get_permi(l):
    assert len(l) == 8
    possi = set()
    for z in permutations(l):
        if z[1] < z[0]:
            continue
            z[0], z[1] = z[1], z[0]
        if z[3] < z[2]:
            continue
            z[2], z[3] = z[3], z[2]
        if z[5] < z[4]:
            continue
            z[4], z[5] = z[5], z[4]
        if z[7] < z[6]:
            continue
            z[6], z[7] = z[7], z[6]
        possi.add(tuple(z))
    return possi
def get_possibe_pairs_for_swaps(n):
    l = list(range(n))
    PAIRS = 8
    for z in combinations(l, PAIRS):
        for x in get_permi(z):
            yield x
    
def get_p2(day_input: list[str]):
    data, wires = extract_data(day_input)
    ori_data = copy.deepcopy(data) 
    working_data = copy.deepcopy(ori_data)

    xx = get_number_value(data, 'x')
    yy = get_number_value(data, 'y')
    z = get_value(data)
    correct_z = xx + yy # '0b1010110'
    wrong = []
    for x in data:
        if x[0] == 'z':
            b = int(x[1:])
            if z & (1 << b) != correct_z & (1 << b):
                wrong.append(x)
    print(wrong)
    
             
     


@pytest.mark.parametrize('day_input, output', [
    # (obtain_lines('3'), 'z00,z01,z02,z05'),
    (obtain_lines(), 222),
])
def test_d24_y2024_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

                                