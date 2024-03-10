import pytest
from d2 import get_game_data, Game, valid_game


def test_get_game_data():
    input_game = "  33 green, 4 blue, 1 red   "

    game: Game = get_game_data(input_game)
    assert game["green"] == 33
    assert game["blue"] == 4
    assert game["red"] == 1


@pytest.mark.parametrize(
    "input_game, expected_output",
    [
        ("  3 green, 4 blue, 1 red   ", True),
        ("  3 green, 4 blue, 13 red   ", False),
        ("  14 green, 4 blue, 1 red   ", False),
        ("  3 green, 14 blue, 1 red   ", False),
    ],
)
def test_valid_game(input_game, expected_output):
    assert valid_game(input_game) == expected_output
