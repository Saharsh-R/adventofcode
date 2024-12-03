import typer
from utils.fetch_input_files import write_input_file

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def fetch(day: int, year: int = 2024 ):
    write_input_file(year, day)

