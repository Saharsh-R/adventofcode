from typing import Optional
import typer
from utils.cli_utils import get_current_day_if_advent_else_1, get_current_year
from utils.fetch_input_files import write_input_file

app = typer.Typer(no_args_is_help=True)

from typing_extensions import Annotated


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def fetch(
    day: Annotated[
        Optional[int], typer.Argument(min=1, max=25)
    ] = get_current_day_if_advent_else_1(),
    year: Annotated[Optional[int], typer.Argument()] = get_current_year(),
):
    """
    Gets the input file corresponding to day and year and saves it to the correct path.
    """
    write_input_file(year, day)
