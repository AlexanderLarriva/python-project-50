from .diff_files import make_diff
from .check_files import check_file


def generate_diff(filepath1, filepath2):
    file1 = check_file(filepath1)
    file2 = check_file(filepath2)
    return make_diff(file1, file2)
