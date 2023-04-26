import os
from gendiff.diff_files import make_diff
from gendiff.parser import parse_file


def test_generate_diff():
    filepath1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
    
    filepath2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
    dict1 = parse_file(filepath1)
    dict2 = parse_file(filepath2)
    
    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'expected_output.txt'), 'r') as diff:
        expected_output = diff.read().strip()
      
    assert make_diff(dict1, dict2) == expected_output

# import pytest

# @pytest.fixture
# def filepath1():
#     return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
