# Day 21, Year 2024
# put example test cases here in 1.txt in the same folder
# by default is input.txt

from functools import cache
import pytest

from utils.generic_functions import obtain_lines

numpad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['', '0', 'A'],
]
keypad = [
    ['', '^', 'A'],
    ['<', 'v', '>'],
]

@cache
def get_numpad_coord(c):
    n, m = len(numpad), len(numpad[0])
    for i in range(n):
        for j in range(m):
            if numpad[i][j] == c:
                return i, j
    assert f'{c} not found in the numpad'

@cache
def get_keypad_coord(c):
    n, m = len(keypad), len(keypad[0])
    for i in range(n):
        for j in range(m):
            if keypad[i][j] == c:
                return i, j
    assert f'{c} not found in the keypad'

def get_numpad_seq(seq) -> str:
    a, b = 3, 2
    ans = []
    for c in seq:
        x, y= get_numpad_coord(c)
        ans.append(get_seq_to_go_from(a, b, x, y, True))
        # ans.append(get_seq_to_go_from(x, y, a, b, True))
        a, b = x, y
    # go up and go right
    return ''.join(ans)

@cache
def get_seq_to_go_from(a, b, x, y,is_keypad):
    ans = ''
    dead_x, dead_y = get_keypad_coord('') if not is_keypad else get_numpad_coord('')

    def hori():
        nonlocal ans

        if b > y:
            ans += '<' * (b - y)
        elif b < y:
            ans += '>' * (y - b)
    
    def veri():
        nonlocal ans
        if a < x:
            ans += 'v' * (x - a)
        elif a > x:
            ans += '^' * (a - x)

    if (a, y) == (dead_x, dead_y):
        veri()
        hori()
    else:
        hori()
        veri()
    return ans  + 'A'

def get_sequence(seq, is_keypad )-> str:
    if is_keypad:
        return get_numpad_seq(seq)
    a, b = 0, 2
    ans = []
    for c in seq:
        x, y = get_keypad_coord(c)
        ans.append(get_seq_to_go_from(a, b, x, y ,False ))
        # ans.append(get_seq_to_go_from(x, y, a, b ,False ))

        a, b = x, y
    # go down and go right

    return ''.join(ans)
    
    



your_pad = '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'
second_d_pad = 'v<<A>>^A<A>AvA<^AA>A<vAAA>^A'
first_d_pad = '<A^A>^^AvvvA'
num_pad = '029A'

testing_seq = [num_pad, first_d_pad, second_d_pad, your_pad]
@pytest.mark.parametrize('input, output', [
    [(testing_seq[0], True),testing_seq[1]],
    [(testing_seq[1], False),testing_seq[2]],
    [(testing_seq[2], False),testing_seq[3]],
])
def test_get_sequence(input, output):
    a, b= input
    assert get_sequence(a, b) == output

def get_full_seq(numpad_seq):
    first_seq = get_sequence(numpad_seq, True)
    second_seq = get_sequence(first_seq, False)
    third_seq = get_sequence(second_seq, False)
    return third_seq , int(numpad_seq[:-1])

@pytest.mark.parametrize('input, output', [
    ['179A', ('<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A', 179)],
    ['456A', ('<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A', 456)],
])
def test_get_full_seq(input, output):
    seq, ext = get_full_seq(input)
    assert seq == output[0]
    assert ext == output[1]



def get_p1(day_input: list[str]):
    l = []
    for numpad_seq in day_input:
        l.append(get_full_seq(numpad_seq))
    return l
        


@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 126384),
    (obtain_lines(), 231564),
])
def test_d21_y2024_p1(day_input: list[str], output: int):
    result = get_p1(day_input)
    ans = 0
    print()
    for a, b in result:
        print(len(a), b, a)
        ans += len(a) * b
    print()
    assert ans == output

def get_p2(day_input: list[str]):
    return 222

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 2),
    (obtain_lines(), 222),
])
def test_d21_y2024_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

                                