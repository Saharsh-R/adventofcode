# Day 23, Year 2024
# put example test cases here in 1.txt in the same folder
# by default is input.txt
from itertools import combinations
from collections import defaultdict
import pytest

from utils.generic_functions import obtain_lines


def get_p1(day_input: list[str]):
    graph = defaultdict(list)
    nodes = {} 
    for x in day_input:
        a, b = x.split('-')
        print(a, b)
        graph[b].append(a)
        graph[a].append(b)
        nodes[a] = 0
        nodes[b] = 0
    assert len(nodes)
    visited = set()
    node_id = 1

    def dfs(node, node_id):
        visited.add(node)
        nodes[node] = node_id
        for x in graph[node]:
            if x not in visited:
                dfs(x, node_id)

    for x in nodes:
        if x not in visited:
            dfs(x, node_id)
            node_id += 1

    store = set()
    for x in nodes:
        if 't' in x[0]:
            for a, b in combinations(graph[x], 2):
                zoo = [a, b, x]
                if b in graph[a]:
                    store.add(tuple(sorted(zoo)))
    return len(store)







    


@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 7),
    (obtain_lines(), 111),
])
def test_d23_y2024_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

from functools import cache

@cache
def get_sorted_tuple(compo, x):
    return tuple(sorted(compo + (x,)))

def get_p2(day_input: list[str]):
    graph = defaultdict(set)
    nodes = {} 
    edges = []
    components = []
    for x in day_input:
        a, b = x.split('-')
        graph[b].add(a)
        graph[a].add(b)
        nodes[a] = 0
        nodes[b] = 0
        edges.append((a, b))
    for a,b  in edges:
        components.append(((a, b), graph[a] & graph[b]))
    assert len(nodes)
    visited = set()

    def dfs(node, node_id):
        visited.add(node)
        for x in graph[node]:
            if x not in visited:
                dfs(x, node_id)

    for x in nodes:
        if x not in visited:
            dfs(x, 0)
    processed = set()
    
    for goo, potential in components:
        for x in goo:
            potential |= graph[x]
        for y in potential:
            if y not in goo:
                new_po_component = get_sorted_tuple(goo, y)
                if new_po_component not in processed:
                    processed.add(new_po_component)
                    if all(z in graph[y] for z in goo):
                        components.append((new_po_component, potential & graph[y]))
    result =components[-1]
    zoo = ','.join(sorted(result[0]))
    return zoo




    return 222

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 'co,de,ka,ta'),
    (obtain_lines(), 'ar,cd,hl,iw,jm,ku,qo,rz,vo,xe,xm,xv,ys'),
])
def test_d23_y2024_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

                                