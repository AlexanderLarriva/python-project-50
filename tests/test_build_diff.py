import os
from gendiff.build_diff import generate_diff


def test_build_diff():
    filepath1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
    filepath2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')
    
    with open(os.path.join(os.path.dirname(__file__), 'fixtures',
                           'expected_output_stylish.txt'), 'r') as diff:
        expected_output_stylish = diff.read().strip()
        
    with open(os.path.join(os.path.dirname(__file__), 'fixtures',
                           'expected_output_plain.txt'), 'r') as diff:
        expected_output_plain = diff.read().strip()
        
    with open(os.path.join(os.path.dirname(__file__), 'fixtures',
                           'expected_output_json.txt'), 'r') as diff:
        expected_output_json = diff.read().strip()
    
    
    assert generate_diff(filepath1, filepath2, 'stylish') == expected_output_stylish
    assert generate_diff(filepath1, filepath2, 'plain') == expected_output_plain
    assert generate_diff(filepath1, filepath2, 'json') == expected_output_json