import re
from collections import defaultdict
from functools import reduce
import operator

from ..generic_functions import obtain_lines


def get_numbers(input_line: str) -> list[re.Match]:
    """
    returns list of all the numbers in the input_line
    """
    return [match for match in re.finditer(r"\d+", input_line)]


def get_symbol(input_line: str) -> list[re.Match]:
    """
    returns list of all the symbols in the input_line
    """
    regex_pattern = r"[^\d.]"

    return [match for match in re.finditer(regex_pattern, input_line)]


def clean_up(numbers: list[re.Match], y_index: int) -> list[re.Match]:
    """
    removes the numbers that are not valid
    """
    result = []
    for match in numbers:
        if match.start() <= y_index + 1 and y_index - 1 <= match.end() - 1:
            result.append(match)
        else:
            continue
    return result


def give_result(path: str) -> int:
    """
    takes the file path and returns the result of our logic d3
    """
    input_lines = obtain_lines(path)

    n, m = len(input_lines), len(input_lines[0])
    valid = [[False] * m for _ in range(n)]

    for i, line in enumerate(input_lines):
        symbol_matches = get_symbol(line)
        for match in symbol_matches:
            y_index = match.start()
            for x in (i - 1, i, i + 1):
                for y in range(y_index - 1, y_index + 2):
                    if 0 <= x < n and 0 <= y < m:
                        valid[x][y] = True

    for x in valid:
        print(*("T" if y else "." for y in x), sep="")
    # pylint: disable=pointless-string-statement
    """ 
    following is the output of the above print statement

    ..TTT.....
    ..TTT.....
    ..TTTTTT..
    ..TTTTTT..
    ..TTTTTT..
    ..TTTTT...
    ....TTT...
    ..TTTTT...
    ..TTTTT...
    ..TTTTT...

    """

    # allowed_ranges = [(match.start() - 1, match.start() + 1) for match in symbol_matches]
    # for match in symbol_matches:
    #     y_index = match.start()
    #     for x in (i - 1, i, i + 1):
    #         number_data[x] = clean_up(number_data[x], y_index)

    ans = 0
    for i, line in enumerate(input_lines):
        number_matches = get_numbers(line)
        for match in number_matches:
            if any(valid[i][y] for y in range(match.start(), match.end())):
                ans += int(match.group())
    return ans


def give_result_part2(path: str) -> int:
    """
    takes the file path and returns the result of our logic d3 part 2
    """
    input_lines = obtain_lines(path)

    number_data: defaultdict[int, list[re.Match]] = defaultdict(list)
    for i, line in enumerate(input_lines):
        number_data[i] = get_numbers(line)

    ans = 0

    for i, line in enumerate(input_lines):
        symbol_matches = get_symbol(line)
        for match in symbol_matches:
            y_index = match.start()
            gears: list[str] = []
            for x in (i - 1, i, i + 1):
                if len(gears) == 3:
                    break
                for number_match in number_data[x]:
                    if (
                        number_match.start() <= y_index + 1
                        and y_index - 1 <= number_match.end() - 1
                    ):
                        gears.append(number_match.group())
                        if len(gears) == 3:
                            break
            if len(gears) == 2:
                ans += reduce(operator.mul, map(int, gears), 1)

    return ans
