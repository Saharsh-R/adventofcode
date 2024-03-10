import re
from typing import TypedDict
from collections import Counter
from pathlib import Path


class Game(TypedDict):
    red: int
    green: int
    blue: int


def get_game_id_if_valid(full_game: str) -> int:
    """
    if game is valid returs the id of the game else 0
    """
    game_id_str, game_str = full_game.split(":")
    games = game_str.split(";")
    if all(valid_game(game) for game in games):
        return int(re.search(r"\d+", game_id_str).group())

    return 0


def get_game_power(full_game: str) -> int:
    """
    if game is valid returs the id of the game else 0
    """
    game_id_str, game_str = full_game.split(":")
    games = game_str.split(";")
    red = 1
    blue = 1
    green = 1
    for game in games:
        game_data = get_game_data(game)
        red = max(red, game_data["red"])
        blue = max(blue, game_data["blue"])
        green = max(green, game_data["green"])

    return red * blue * green


RED = 12
GREEN = 13
BLUE = 14


def valid_game(game):
    """
    asserts if a game string like "  33 green, 4 blue, 1 red   " is valid
    """
    game_data: Game = get_game_data(game)
    return (
        game_data["red"] <= 12 and game_data["green"] <= 13 and game_data["blue"] <= 14
    )


def get_game_data(game: str) -> Game:
    """
    expects something like  - 2 red, 1 blue, 10 green
    """
    data = re.findall(r"(\d+) (red|green|blue)", game)
    game_data: Game = Counter()
    for count, color in data:
        game_data[color] += int(count)
    return game_data


parent_dir = Path(__file__).resolve().parent
input_file = parent_dir / f"{parent_dir.name}_input.txt"


def perform_operation(file_path: Path, part2 = False) -> int:
    """
    takes the file path and returns the sum of the two digit numbers
    """
    with file_path.open("r", encoding="utf-8") as file:
        return sum(get_game_power(line) if part2 else get_game_id_if_valid(line) for line in file)


# print(perform_operation(input_file)) # 2237

# print(perform_operation(input_file, True)) # 66681