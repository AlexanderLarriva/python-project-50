DEFAULT_INDENT = 4


def to_str(value, level: int) -> str:
    if isinstance(value, dict):
        lines = ['{']
        for key, nested_value in value.items():
            if isinstance(nested_value, dict):
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
    OPERATIONS = {
        'same': lambda x, y: line_forming(x, 'value', y, sign='    '),
        'add': lambda x, y: line_forming(x, 'new', y, sign='  + '),
        'removed': lambda x, y: line_forming(x, 'old', y, sign='  - '),
        'changed': lambda x, y: '\n'.join([
            line_forming(x, 'old', y, sign='  - '),
            line_forming(x, 'new', y, sign='  + ')
        ]),
        'nested': lambda x, y: (
            f'{" " * y}    {x["key"]}: '
            f'{build_stylish_iter(x["value"], y + DEFAULT_INDENT)}'
        )
    }

    result = ['{']
    for dictionary in diff:
        operation = dictionary['operation']

        if operation in OPERATIONS:
            result.append(OPERATIONS[operation](dictionary, level))

    result.append(f'{" " * level}}}')
    return '\n'.join(result)


def to_stylish(diff: dict) -> str:
    return build_stylish_iter(diff)