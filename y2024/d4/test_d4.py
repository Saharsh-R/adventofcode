import pytest

from utils.generic_functions import obtain_lines


@pytest.fixture
def matrix():
    return obtain_lines()


def test_few_elements(matrix):
    assert matrix[0][1] == "M"
    assert matrix[1][-1] == "A"


SAMPE_TEST_CASE = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]

SAMPLE_TEST_2 = [
    "SAAA",
    "AAAA",
    "MAAA",
    "XAAA",
]


def get_c(left: int) -> str:
    if left == 4:
        return "X"
    elif left == 3:
        return "M"
    elif left == 2:
        return "A"
    elif left == 1:
        return "S"
    return ""


def get_xmas(mat: list[str]) -> int:
    if not mat:
        return 0

    n, m = len(mat), len(mat[0])

    def dfs(i: int, j: int, left: int) -> int:
        c = get_c(left)
        if c == mat[i][j] == "S":
            return 1
        if mat[i][j] != c:
            return 0
        ans = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                a, b = dx + i, dy + j
                if (dx or dy) and 0 <= a < n and 0 <= b < m:
                    ans += dfs(a, b, left - 1)
        return ans

    ans = 0
    for i in range(n):
        for j in range(m):
            ans += dfs(i, j, 4)
    return ans


def get_xmas_straight(mat: list[str]) -> int:
    def is_okay(i, j, dx, dy):
        if mat[i][j] != "X":
            return False
        if mat[i + dx][j + dy] != "M":
            return False
        if mat[i + 2 * dx][j + 2 * dy] != "A":
            return False
        if mat[i + 3 * dx][j + 3 * dy] != "S":
            return False
        return True

    if not mat:
        return 0
    n, m = len(mat), len(mat[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    if not (n > 3 * dx + i >= 0 <= j + dy * 3 < m):
                        continue
                    if is_okay(i, j, dx, dy):
                        ans += 1
    return ans


def get_crosses(mat: list[str]) -> int:
    def is_cross(i: int, j: int) -> bool:
        checks = [
            [(0, 0, "M"), (0, 2, "S"), (1, 1, "A"), (2, 0, "M"), (2, 2, "S")],
            [(0, 0, "S"), (0, 2, "M"), (1, 1, "A"), (2, 0, "S"), (2, 2, "M")],
            [(0, 0, "S"), (0, 2, "S"), (1, 1, "A"), (2, 0, "M"), (2, 2, "M")],
            [(0, 0, "M"), (0, 2, "M"), (1, 1, "A"), (2, 0, "S"), (2, 2, "S")],
        ]

        def is_all_good(check) -> bool:
            for dx, dy, c in check:
                if mat[i + dx][j + dy] != c:
                    return False
            return True

        for check in checks:
            if is_all_good(check):
                return True
        return False

    if not mat:
        return 0
    n, m = len(mat), len(mat[0])
    ans = 0
    for i in range(0, n - 2):
        for j in range(0, m - 2):
            if is_cross(i, j):
                ans += 1
    return ans


@pytest.mark.parametrize(
    "mat, ans", [(SAMPE_TEST_CASE, 18), (SAMPLE_TEST_2, 1), (obtain_lines(), 2458)]
)
def test_get_xmas(mat, ans):
    assert get_xmas_straight(mat) == ans


@pytest.mark.parametrize(
    "mat, ans", [(SAMPE_TEST_CASE, 9), (SAMPLE_TEST_2, 0), (obtain_lines(), 1945)]
)
def test_get_cross(mat, ans):
    assert get_crosses(mat) == ans
