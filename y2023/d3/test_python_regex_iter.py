import re


def test_iter_regex():
    line = ".......242....43...6.....+..34"
    regex_pattern = r"\d+"
    findall_result = re.findall(regex_pattern, line)
    assert findall_result == ["242", "43", "6", "34"]

    finditer_result = [x for x in re.finditer(regex_pattern, line)]
    assert finditer_result != ["242", "43", "6", "34"]
    for match in finditer_result:
        assert type(match) == re.Match
        assert isinstance(match.start(), int)
        assert isinstance(match.end(), int)
        assert match.start() < match.end()

    first_match = finditer_result[0]
    assert first_match.group() == "242"
    assert first_match.start() == 7
    assert first_match.end() == 10
    assert first_match.span() == (first_match.start(), first_match.end()) == (7, 10)
    length_of_group = first_match.end() - first_match.start()
    assert length_of_group == 3


def test_regex_negative_match():
    line = "232..23+.a*"
    regex_pattern = r'[^\d.]'
    findall_result = re.findall(regex_pattern, line)
    assert findall_result == ["+", "a", "*"]

    find_iter_result = [x for x in re.finditer(regex_pattern, line)]
    assert find_iter_result != ["+", "a", "*"]
    assert len(find_iter_result) == 3
    second_match = find_iter_result[1]
    assert second_match.group() == "a"
    assert second_match.start() == 9
    assert second_match.end() == 10