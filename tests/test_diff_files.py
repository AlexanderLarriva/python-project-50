import os
from gendiff.diff_files import make_diff
from gendiff.parser import parse_file


def test_generate_diff():
    filepath1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
    
    filepath2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
    dict1 = parse_file(filepath1)
    dict2 = parse_file(filepath2)
    # продумать с фикстурами. Вывод реально большой.
    expected_output = """{\n  - follow: False\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: True\n}""".strip()

    
    assert make_diff(dict1, dict2) == expected_output

# import pytest

# @pytest.fixture
# def filepath1():
#     return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
