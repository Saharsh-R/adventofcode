# Day 22, Year 2024
# put example test cases here in 1.txt in the same folder
# by default is input.txt

from collections import Counter
import pytest

from utils.generic_functions import obtain_lines

def mix_number(value, secret_number):
    return  value ^ secret_number

def test_mix_number():
    assert mix_number(15, 42) == 37

def get_next(x):
    
    x = x ^ (x * 64)
    x %= 16777216

    x = x ^ (x // 32)
    x %= 16777216   

    x = x ^ (x * 2048)
    x %= 16777216   
    return x

def get_secrets(x):
    ans = []
    while len(ans) < 2000:
        x = get_next(x)
        ans.append(x)
    return ans

def test_get_secrets():
    z = get_secrets(123)
    assert z[:10] == [
        15887950,
        16495136,
        527345,
        704524,
        1553684,
        12683156,
        11100544,
        12249484,
        7753432,
        5908254,
    ]

def get_p1(day_input: list[str]):
    ans = 0
    for x in day_input:
        x = int(x)
        secrets = get_secrets(x)
        ans += secrets[1999]
    return ans

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 37327623),
    (obtain_lines(), 111),
])
def test_d22_y2024_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

def get_four(data:list[int]):
    data = [x % 10 for x in data]
    store = Counter()
    for i in range(4, len(data)):
        a, b, c, d, e= data[i-4:i +1]
        key = b -a, c - b, d - c, e - d
        if key not in store:
            store[key] += e 
    return store


def get_p2(day_input: list[str]):
    zoo = Counter()
    for x in day_input:
        x = int(x)
        secrets = get_secrets(x)
        zoo += get_four(secrets)

    return max(zoo.values())

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('2'), 23),
    (obtain_lines(), 222),
])
def test_d22_y2024_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

                                