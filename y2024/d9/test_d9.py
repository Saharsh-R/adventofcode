import pytest

from utils.generic_functions import obtain_lines

TEST_INPUT = "2333133121414131402"


def get_check_sum_compressed(s: str) -> list[int]:
    if len(s) % 2 == 0:
        assert False
        s = s[:-1]
    system: list[int] = []
    empty_spaces: deque[int] = deque()
    filled: list[int] = []
    for i, d in enumerate(s):
        if i % 2:
            # space
            for _ in range(int(d)):
                empty_spaces.append(len(system))
                system.append(0)
        else:
            # file
            f_id = i // 2
            for _ in range(int(d)):
                filled.append(len(system))
                system.append(f_id)
    while empty_spaces:
        digit_i = filled.pop()
        empty_i = empty_spaces.popleft()
        if digit_i < empty_i:
            break
        system[empty_i] = system[digit_i]
        system[digit_i] = 0
    while system[-1] == 0:
        system.pop()
    return system


def get_full_compacted(s: str) -> list[int]:
    system: list[int] = []
    empty_spaces: list[tuple[int, int]] = []  # index, spaces_empty
    files: list[tuple[int, int]] = []  # index, size of file
    for i, d in enumerate(s):
        if i % 2:
            # space
            empty_spaces.append((len(system), int(d)))
            for _ in range(int(d)):
                system.append(0)
        else:
            # file
            f_id = i // 2
            files.append((len(system), int(d)))
            for _ in range(int(d)):
                system.append(f_id)
    while files:
        starting_index, file_size = files.pop()
        for ijk, (i, spaces_empty) in enumerate(empty_spaces):
            if i > starting_index:
                break
            if file_size <= spaces_empty:
                system[i : i + file_size] = system[
                    starting_index : starting_index + file_size
                ]
                system[starting_index : starting_index + file_size] = [0] * file_size
                empty_spaces[ijk] = (i + file_size, spaces_empty - file_size)
                break

    while system[-1] == 0:
        system.pop()
    return system


def get_p1_value(s: str) -> int:
    return sum(i * d for i, d in enumerate(get_check_sum_compressed(s)))


def get_p2_value(s: str) -> int:
    return sum(i * d for i, d in enumerate(get_full_compacted(s)))


def get_array_from_s(s: str) -> list[int]:
    ans = []
    for c in s:
        if c == ".":
            ans.append(0)
        else:
            ans.append(int(c))
    return ans


@pytest.mark.parametrize(
    "input, output",
    [
        ("12345", [0, 2, 2, 1, 1, 1, 2, 2, 2]),
        (
            TEST_INPUT,
            [
                0,
                0,
                9,
                9,
                8,
                1,
                1,
                1,
                8,
                8,
                8,
                2,
                7,
                7,
                7,
                3,
                3,
                3,
                6,
                4,
                4,
                6,
                5,
                5,
                5,
                5,
                6,
                6,
            ],
        ),
    ],
)
def test_system(input, output):
    assert get_check_sum_compressed(input) == output


@pytest.mark.parametrize(
    "input, output", [(TEST_INPUT, 1928), (obtain_lines()[0], 6288599492129)]
)
def test_d9_24_p1(input, output):
    assert get_p1_value(input) == output


@pytest.mark.parametrize(
    "input, output",
    [
        ("12345", [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2, 2]),
        (TEST_INPUT, get_array_from_s("00992111777.44.333....5555.6666.....8888")),
    ],
)
def test_system_p2(input, output):
    assert get_full_compacted(input) == output


@pytest.mark.parametrize(
    "input, output", [(TEST_INPUT, 2858), (obtain_lines()[0], 6321896265143)]
)
def test_d9_24_p2(input, output):
    assert get_p2_value(input) == output
