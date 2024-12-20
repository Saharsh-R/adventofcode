import os
from pathlib import Path
from rich import print
import requests
from dotenv import load_dotenv

load_dotenv()

cookies = {"session": os.getenv("AOC_SESSION_COOKIE")}


parent_dir = Path(__file__).resolve().parent.parent


def write_input_file(year: int, day: int):
    assert year > 2000, f"The input year is {year}, please provide 4 digit year"
    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        cookies=cookies,
        timeout=5,
        verify=False,
    )
    if response.status_code == 200:
        dev_dir = parent_dir / f"y{year}" / f"d{day}"
        input_file_path = dev_dir / f"input.txt"
        code_path = dev_dir / f"test_d{day}_y{year}.py"
        input_file_path.parent.mkdir(parents=True, exist_ok=True)

        test_case_file = dev_dir / "1.txt"
        print()
        print(f'Question at https://adventofcode.com/{year}/day/{day}')

        with open(input_file_path, "w", encoding="utf-8") as file:
            file.write(response.text)
            print(f"Data of day {day}, year {year} written to file successfully to {input_file_path}")
        if not code_path.exists():
            with open(code_path, "w", encoding="utf-8") as code_file:
                code_file.write(f"""# Day {day}, Year {year}
# put example test cases here in 1.txt in the same folder
# by default is input.txt

import pytest

from utils.generic_functions import obtain_lines


def get_p1(day_input: list[str]):
    return 111

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 1),
    (obtain_lines(), 111),
])
def test_d{day}_y{year}_p1(day_input: list[str], output: int):
    assert get_p1(day_input) == output

def get_p2(day_input: list[str]):
    return 222

@pytest.mark.parametrize('day_input, output', [
    (obtain_lines('1'), 2),
    (obtain_lines(), 222),
])
def test_d{day}_y{year}_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output

                                """)

        open(test_case_file, "a").close()  # create an empty file
        print(f"Test case file made at {test_case_file}")

        print(f"Code at {code_path}")
    else:
        print(f"Failed to fetch data for day {day}, year {year} , status code: {response.status_code}")
        print(f"Error reason: {response.reason}")
