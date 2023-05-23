from .files import prepare_data
from .parser import parse_file
from .diff_files import compare_dicts
from .formats import get_formatter


def generate_diff(filepath1: str, filepath2: str,
                  formater: str = 'stylish') -> str:
    data1, format1 = prepare_data(filepath1)
    data2, format2 = prepare_data(filepath2)
    dict1 = parse_file(data1, format1)
    dict2 = parse_file(data2, format2)
    diff = compare_dicts(dict1, dict2)
    return get_formatter(formater)(diff)
