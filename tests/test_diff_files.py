import os
from gendiff.diff_files import generate_diff


def test_generate_diff():
    filepath1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
    
    filepath2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
    
    expected_output = f"""gendiff {filepath1} {filepath2}
{{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}}"""
    
    assert generate_diff(filepath1, filepath2) == expected_output

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

