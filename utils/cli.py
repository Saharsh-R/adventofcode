import typer
from utils.fetch_input_files import write_input_file

app = typer.Typer(no_args_is_help=True)


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def fetch(day: int, year: int = 2024):
    """
    Gets the input file corresponding to day and year and saves it to the correct path.
    """
    write_input_file(year, day)
