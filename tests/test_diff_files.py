import os
from gendiff.diff_files import make_diff
from gendiff.parser import parse_file
from gendiff.date_prepare import prepare_data


def test_generate_diff():
    filepath1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
    filepath2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
    data1, format1 = prepare_data(filepath1)
    data2, format2 = prepare_data(filepath2)
    # Получаем словари из парсера
    dict1 = parse_file(data1, format1)  # dict
    dict2 = parse_file(data2, format2)
    
    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'expected_output.txt'), 'r') as diff:
        expected_output = diff.read().strip()
      
    assert str(make_diff(dict1, dict2)) == expected_output

# import pytest

# @pytest.fixture
# def filepath1():
#     return os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
