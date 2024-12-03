from utils.generic_functions import obtain_lines
from .d3 import give_result, give_result_part2
import pytest


def test_test_data():
    assert obtain_lines("test") == ["banana", "zoom ", "   apple", "\\n"]


@pytest.mark.skip(reason="don't recompute")
def test_example_data():
    assert give_result("example") == 4361


@pytest.mark.skip(reason="don't recompute")
def test_input_data():
    assert give_result("input") == 525181


@pytest.mark.skip(reason="don't recompute")
def test_2_example():
    assert give_result_part2("example") == 467835


@pytest.mark.skip(reason="don't recompute")
def test_2_input():
    assert give_result_part2("input") == 84289137
