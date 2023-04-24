import os
from gendiff.diff_files import make_diff
from gendiff.parser import parse_file


def test_generate_diff():
    filepath1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
    
    filepath2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
    dict1 = parse_file(filepath1)
    dict2 = parse_file(filepath2)
    name_file1 = os.path.basename(filepath1)
    name_file2 = os.path.basename(filepath2)
    expected_output = f"""gendiff file1.json file2.json
{{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}}"""
    
    assert make_diff(dict1, dict2, name_file1, name_file2) == expected_output

# import pytest

# @pytest.fixture
# def filepath1():
#     return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')

# @pytest.fixture
# def filepath2():
#     return os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')

# @pytest.fixture
# def expected_output():
#     return f"""gendiff {filepath1} {filepath2}
# {{
#   - follow: False
#     host: hexlet.io
#   - proxy: 123.234.53.22
#   - timeout: 50
#   + timeout: 20
#   + verbose: True
# }}"""

# def test_generate_diff(filepath1, filepath2, expected_output):
#     assert generate_diff(filepath1, filepath2) == expected_output

