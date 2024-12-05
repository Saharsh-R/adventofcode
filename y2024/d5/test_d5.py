from collections import defaultdict, deque
from email.policy import default
import pytest
from requests import get

from utils.generic_functions import obtain_lines


def get_test_cases():
    order = []
    lines = []

    for s in obtain_lines():
        if '|' in s:
            order.append(list(map(int, s.split('|'))))
        elif s:
            lines.append(list(map(int, s.split(','))))
    return order, lines

def test_input():
    order, lines = get_test_cases()
    assert len(order) == 1176
    assert len(lines) == 189
    for x in lines:
        assert len(x) % 2 == 1
        assert len(set(x)) == len(x)

def get_mid(l: list[int]) -> int:
    return l[len(l) // 2]


def is_line_correct(l: list[int], orders) -> bool:
    l_set = set(l)
    for a, b in orders:
        if a in l_set and b in l_set:
            if l.index(a) > l.index(b):
                return False
    return True

def test_get_mid():
    assert get_mid([1, 2, 3, 4, 5]) == 3
    assert get_mid([1, 2, 3, 4, 5, 6]) == 4


def test_d5_24_p1():
    order, lines = get_test_cases()
    ans = 0
    for x in lines:
        if is_line_correct(x, order):
            ans += get_mid(x)
    assert ans == 0




def topo_sort(orders: list[tuple[int, int]], line: list[int])->list[int]:
    pre: defaultdict[int, set[int]] = defaultdict(set)
    nex: defaultdict[int, set[int]] = defaultdict(set)
    for a, b in orders:
        pre[b].add(a)
        nex[a].add(b)
    q:deque[int] = deque()
    ans :list[int]= []
    for x in line:
        if not pre[x]:
            q.append(x)
    assert len(q) != 0
    while q:
        x = q.popleft()
        ans.append(x)
        for y in nex[x]:
            pre[y].remove(x)
            if not pre[y]:
                q.append(y)
    assert len(ans) == len(line)
    return ans

def get_useful_orders(orders: list[tuple[int, int]], line:list[int]) ->list[tuple[int, int]]:
    store = set(line)
    return [(a,b) for a, b in orders if (a in store and b in store)]


def test_d5_24_p2():
    order, lines = get_test_cases()
    ans = 0
    for x in lines:
        if is_line_correct(x, order):
            continue
        filtered = get_useful_orders(order, x)
        corrected = topo_sort(filtered, x)
        ans += get_mid(corrected)
    assert ans == 0

