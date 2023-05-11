import pytest
from gendiff.date_prepare import prepare_data
from tests import get_fixture_path


def test_date_prepare():
    filepath1 = get_fixture_path('file1.json')
    filepath2 = get_fixture_path('file1.yml')
    filepath3 = get_fixture_path('expected_output_plain.txt')

    with open(filepath1) as f:
        data1 = f.read()

    with open(filepath2) as f:
        data2 = f.read()

    assert prepare_data(filepath1) == (data1, 'json')
    assert prepare_data(filepath2) == (data2, 'yml')

    with pytest.raises(ValueError) as e_info:
        prepare_data(filepath3)
    assert str(e_info.value) == "Unrecognized extension: txt"
