import inspect
from pathlib import Path


def obtain_lines(file_name: str = "input") -> list[str]:
    """
    takes the file path and returns an array of lines (the last \n is removed)
    """
    caller_file = Path(
        inspect.stack()[1].filename
    )  # where this function is being called from
    parent_dir = caller_file.resolve().parent
    input_file = parent_dir / f"{file_name}.txt"
    with input_file.open("r", encoding="utf-8") as file:
        return [line.rstrip("\n") for line in file]
