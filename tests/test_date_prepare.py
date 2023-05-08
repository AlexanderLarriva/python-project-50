import os
import pytest
from gendiff.date_prepare import prepare_data


def test_date_prepare():
    filepath1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
    filepath2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.yml')
    filepath3 = os.path.join(os.path.dirname(__file__), 'fixtures', 'expected_output_plain.txt')

    with open(filepath1) as f:
        data1 = f.read()

    with open(filepath2) as f:
        data2 = f.read()

    assert prepare_data(filepath1) == (data1, 'json')
    assert prepare_data(filepath2) == (data2, 'yml')

    with pytest.raises(ValueError) as e_info:
        prepare_data(filepath3)
    assert str(e_info.value) == "Unrecognized extension: txt"
