from gendiff.diff_files import compare_dicts
from gendiff.parser import parse_file
from gendiff.files import prepare_data
from tests import get_fixture_path


def test_generate_diff():
    filepath1 = get_fixture_path('file1.json')
    filepath2 = get_fixture_path('file2.json')
    data1, format1 = prepare_data(filepath1)
    data2, format2 = prepare_data(filepath2)
    dict1 = parse_file(data1, format1)
    dict2 = parse_file(data2, format2)

    with open(get_fixture_path('expected_output.txt'), 'r') as diff:
        expected_output = diff.read().strip()

    assert str(compare_dicts(dict1, dict2)) == expected_output
