from pathlib import Path

input_file = Path(__file__).parent / "d1_input.txt"


def parse_value_from_string(string: str) -> int:
    """
    takes the occurence of first integer and last integer in the string
    and returns the two digit numbe
    """
    first_occ = next(c for c in string if c.isdigit())
    last_occ = next(c for c in reversed(string) if c.isdigit())
    return int(first_occ + last_occ)


def obtain_result(file_path: Path) -> int:
    """
    takes the file path and returns the sum of the two digit numbers
    """
    with file_path.open("r", encoding="utf-8") as file:
        return sum(parse_value_from_string(line) for line in file)


print(obtain_result(input_file))
