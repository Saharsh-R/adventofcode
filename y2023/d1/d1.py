from pathlib import Path
import re

input_file = Path(__file__).parent / "d1_input.txt"


def parse_value_from_string_old(string: str) -> int:
    """
    takes the occurence of first integer and last integer in the string
    and returns the two digit numbe
    """
    first_occ = next(c for c in string if c.isdigit())
    last_occ = next(c for c in reversed(string) if c.isdigit())
    return int(first_occ + last_occ)


def regex_matches(
    string: str, regex: str = r"\d|one|two|three|four|five|six|seven|eight|nine"
):
    matches: list[str] = re.findall(regex, string)
    first = str(matches[0]) if matches[0].isdigit() else matches[0]
    last = str(matches[-1]) if matches[-1].isdigit() else matches[-1]
    return first + last


number_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def parse_value_from_string(string: str) -> int:
    """
    takes the occurence of first integer and last integer in the string
    and returns the two digit numbe
    """

    overlapping_regex = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    matches = [match.group(1) for match in re.finditer(overlapping_regex, string)]

    first = (
        str(matches[0]) if matches[0].isdigit() else str(number_to_digit[matches[0]])
    )
    last = (
        str(matches[-1]) if matches[-1].isdigit() else str(number_to_digit[matches[-1]])
    )
    return int(first + last)


def obtain_result(file_path: Path) -> int:
    """
    takes the file path and returns the sum of the two digit numbers
    """
    with file_path.open("r", encoding="utf-8") as file:
        return sum(parse_value_from_string(line) for line in file)


# print(obtain_result(input_file))
