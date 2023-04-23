from .diff_files import build_diff


def generate_diff(filepath1, filepath2):
    return build_diff(filepath1, filepath2)
