import pytest
from tests import get_fixture_path
from gendiff.build_diff import generate_diff

def read_file(filepath):
    with open(filepath) as file:
        return file.read()

plain_expected_output = read_file(get_fixture_path("expected_output_plain.txt")).split("---")
json_expected_output = read_file(get_fixture_path("expected_output_json.txt")).split("---")
stylish_expected_output = read_file(get_fixture_path("expected_output_stylish.txt")).split("---")

@pytest.mark.parametrize(
"format_, first_file, second_file, expected_output",
    [
    ("plain", "file1.json", "file2.json", plain_expected_output[0]),
    ("plain", "file1.yml", "file2.json", plain_expected_output[0]),
    ("plain", "file1.json", "file2.yml", plain_expected_output[0]),
    ("plain", "file1.yml", "file2.yml", plain_expected_output[0]),
    
    ("plain", "file12.json", "file22.json", plain_expected_output[1]),
    ("plain", "file12.yml", "file22.json", plain_expected_output[1]),
    ("plain", "file12.json", "file22.yml", plain_expected_output[1]),
    ("plain", "file12.yml", "file22.yml", plain_expected_output[1]),
    
    ("json", "file1.json", "file2.json", json_expected_output[0]),
    ("json", "file1.yml", "file2.json", json_expected_output[0]),
    ("json", "file1.json", "file2.yml", json_expected_output[0]),
    ("json", "file1.yml", "file2.yml", json_expected_output[0]),
    
    ("json", "file12.json", "file22.json", json_expected_output[1]),
    ("json", "file12.yml", "file22.json", json_expected_output[1]),
    ("json", "file12.json", "file22.yml", json_expected_output[1]),
    ("json", "file12.yml", "file22.yml", json_expected_output[1]),
    
    ("stylish", "file1.json", "file2.json", stylish_expected_output[0]),
    ("stylish", "file1.yml", "file2.json", stylish_expected_output[0]),
    ("stylish", "file1.json", "file2.yml", stylish_expected_output[0]),
    ("stylish", "file1.yml", "file2.yml", stylish_expected_output[0]),
    
    ("stylish", "file12.json", "file22.json", stylish_expected_output[1]),
    ("stylish", "file12.yml", "file22.json", stylish_expected_output[1]),
    ("stylish", "file12.json", "file22.yml", stylish_expected_output[1]),
    ("stylish", "file12.yml", "file22.yml", stylish_expected_output[1]),
    ]
    )
def test_generate_diff(format_, first_file, second_file, expected_output):
    filepath1 = get_fixture_path(first_file)
    filepath2 = get_fixture_path(second_file)
    result = generate_diff(filepath1, filepath2, format_)
    assert result == expected_output.strip()
