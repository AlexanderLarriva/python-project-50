from .diff_files import make_diff
from .parser import parse_file
import os


def generate_diff(filepath1, filepath2):
    dict1 = parse_file(filepath1)  # dict
    dict2 = parse_file(filepath2)  # dict
    name_file1 = os.path.basename(filepath1)
    name_file2 = os.path.basename(filepath2)
    return make_diff(dict1, dict2, name_file1, name_file2)
