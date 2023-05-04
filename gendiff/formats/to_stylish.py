# from typing import Any

DEFAULT_INDENT = 4  # отступ по умолчанию


def to_str(value, level: int) -> str:
    # Если значение является словарем
    if isinstance(value, dict):
        # Вводим список с начальным значением - {
        lines = ['{']
        # Циклом проходим по ключам и значениям словаря - диффа
        for key, nested_value in value.items():
            # Если вложенное значение является словарем
            if isinstance(nested_value, dict):
                # Рекурсивно вызываем функцию to_str
                new_value = to_str(nested_value, level + DEFAULT_INDENT)
                lines.append(f"{' ' * level}    {key}: {new_value}")
            else:
                lines.append(f"{' ' * level}    {key}: {nested_value}")
        lines.append(f'{" " * level}}}')
        return '\n'.join(lines)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def line_forming(dictionary: dict, key, level: int, sign: str) -> str:
    return f'{" " * level}{sign}{dictionary["key"]}: ' \
           f'{to_str(dictionary[key], level + DEFAULT_INDENT)}'


def build_stylish_iter(diff: dict, level=0) -> str:
    result = ['{']
    for dictionary in diff:
        key = dictionary['key']
        value = dictionary.get('value')
        operation = dictionary['operation']

        if operation == 'same':
            result.append(line_forming(dictionary, 'value', level, sign='    '))

        elif operation == 'add':
            result.append(line_forming(dictionary, 'new', level, sign='  + '))

        elif operation == 'removed' or operation == 'changed':
            result.append(line_forming(dictionary, 'old', level, sign='  - '))

            if operation == 'changed':
                result.append(line_forming(dictionary, 'new', level,
                                        sign='  + '))

        elif operation == 'nested':
            new_value = build_stylish_iter(value, level + DEFAULT_INDENT)
            result.append(f'{" " * level}    {key}: {new_value}')

    result.append(f'{" " * level}}}')
    return '\n'.join(result)


def render_stylish(diff: dict) -> str:
    return build_stylish_iter(diff)
