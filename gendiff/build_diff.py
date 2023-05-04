from .date_prepare import prepare_data
from .parser import parse_file
from .diff_files import make_diff
from .formats import get_formatter


def generate_diff(filepath1: str, filepath2: str,
                  formater: str = 'stylish') -> str:
    # Готовим данные
    data1, format1 = prepare_data(filepath1)
    data2, format2 = prepare_data(filepath2)
    # Получаем словари из парсера
    dict1 = parse_file(data1, format1)  # dict
    dict2 = parse_file(data2, format2)  # dict
    # Получаем дифф словарей
    diff = make_diff(dict1, dict2)
    # Возвращаем результат с учетом форматтера
    # return diff
    return get_formatter(formater)(diff)
