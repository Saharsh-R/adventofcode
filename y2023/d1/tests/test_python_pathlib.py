from pathlib import Path


def test_pathlib():
    """
    to test pathlib and see what all can be done
    """
    current_dir = Path(__file__).resolve().parent.parent  # due to test directory
    file_path = current_dir / "d1_input.txt"
    assert file_path.exists()
    assert isinstance(file_path.name, str)
    assert str(file_path).endswith("y2023/d1/d1_input.txt")


def test_str_endswith():
    '''
    to test the endswith method of string
    '''
    a = "2023/1/d1_input.txt"
    assert a.endswith("d1_input.txt")


def test_default_behaviour_pathlib():
    '''
    when resolve is not called it is relative path
    '''
    current_path = Path(__file__)
    assert current_path.exists()
    assert str(current_path).endswith("2023/d1/tests/test_python_pathlib.py")


def test_default_behaviour_pathlib_resolve():
    '''
    when resolve is called it is absolute path
    '''
    current_path = Path(__file__).resolve()
    assert current_path.exists()
    assert str(current_path).endswith("2023/d1/tests/test_python_pathlib.py")



