from itertools import product, combinations
from functools import lru_cache
numeric_keypad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2)
}
direction_keypad = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2)
}

dd = {
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    "^": (-1, 0)
}


def get_combos(ca, a, cb, b):
    # char a, char b, int a, int b
    for idxs in combinations(range(a + b), r=a):
        res = [cb] * (a + b)
        for i in idxs:
            res[i] = ca
        yield "".join(res)


@lru_cache(None)
def generate_ways_utils(a, b, is_numpad):
    keypad = direction_keypad if is_numpad else numeric_keypad

    cur_loc = keypad[a]
    next_loc = keypad[b]
    di = next_loc[0] - cur_loc[0]
    dj = next_loc[1] - cur_loc[1]

    moves = []
    if di > 0:
        moves += ["v", di]
    else:
        moves += ["^", -di]
    if dj > 0:
        moves += [">", dj]
    else:
        moves += ["<", -dj]
    
    raw_combos = list(set(["".join(x) + "A" for x in get_combos(*moves)]))
    combos = []
    for combo in raw_combos:
        ci, cj = cur_loc
        good = True
        for c in combo[:-1]:
            di, dj = dd[c]
            ci, cj = ci + di, cj + dj
            if not (ci, cj) in keypad.values():
                good = False
                break
        if good:
            combos.append(combo)

    return combos