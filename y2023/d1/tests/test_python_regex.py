import re
import pytest


def test_overlapping_matches():

    pattern = r"(?=(two|one))"
    string = "twone"
    sub_step = re.finditer(pattern, string)

    matches = [match.group(1) for match in re.finditer(pattern, string)]
    assert matches == ["two", "one"]


def test_match_search():
    """
    diff between match and search
    """
    pattern = r"\d"
    string = "abc123def"

    search_result = re.search(pattern, string)
    match_result = re.match(pattern, string)

    assert match_result is None
    assert search_result.group() == "1"
    assert search_result.start() == 3  # index
    assert search_result.group(0) == "1"

    with pytest.raises(IndexError):
        # if no capturing groups this will also raise IndexError
        assert search_result.group(-1) == "1"

    with pytest.raises(IndexError):
        assert search_result.group(1) == "2"
    with pytest.raises(IndexError):
        assert search_result.group(2) == "3"


def test_findall():
    pattern = r"\d"
    string = "abc123def9"

    findall_result = re.findall(pattern, string)
    assert findall_result == ["1", "2", "3", "9"]


def test_match():
    """
    diff between match and search
    """
    pattern = r"\d"
    string = "5abc123def"

    match_result = re.match(pattern, string)
    assert match_result is not None
    assert match_result.group() == "5"
    assert match_result.start() == 0


def test_group_match():
    '''
    test multiple group match
    '''
    pattern = r"(\d)(\d)(\d)"
    string = "abc123def"

    search_result = re.search(pattern, string)
    match_result = re.match(pattern, string)

    assert match_result is None
    assert search_result.group() == "123"
    assert search_result.start() == 3  # index
    assert search_result.group(0) == "123"
    assert search_result.group(1) == "1"
    assert search_result.group(2) == "2"
    assert search_result.group(3) == "3"
    with pytest.raises(IndexError):
        assert search_result.group(-1) == "3"
    assert search_result.groups() == ("1", "2", "3")
