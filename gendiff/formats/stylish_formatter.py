DEFAULT_INDENT = 4


def to_str(value, level: int) -> str:
    if isinstance(value, dict):
        result = ['{']
        for key, nested_value in value.items():
            if isinstance(nested_value, dict):
                new_value = to_str(nested_value, level + DEFAULT_INDENT)
                result.append(f"{' ' * level}    {key}: {new_value}")
            else:
                result.append(f"{' ' * level}    {key}: {nested_value}")
        result.append(f'{" " * level}}}')
        return '\n'.join(result)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def line_forming(dictionary: dict, key, level: int, sign: str) -> str:
    return f'{" " * level}{sign}{dictionary["key"]}: ' \
           f'{to_str(dictionary[key], level + DEFAULT_INDENT)}'


def process_operation(operation, dictionary, level, result):
    if operation == 'same':
        result.append(line_forming(
            dictionary, 'value',
            level, sign='    '
        ))

    if operation == 'add':
        result.append(line_forming(
            dictionary, 'new',
            level, sign='  + '
        ))

    if operation == 'removed' or operation == 'changed':
        result.append(line_forming(
            dictionary, 'old',
            level, sign='  - '
        ))

    if operation == 'changed':
        result.append(
            line_forming(
                dictionary, 'new',
                level, sign='  + '
            ))

    if operation == 'nested':
        new_value = to_stylish(dictionary['value'], level + DEFAULT_INDENT)
        result.append(f'{" " * level}    {dictionary["key"]}: {new_value}')


def to_stylish(diff: dict, level=0) -> str:
    result = ['{']
    for dictionary in diff:
        operation = dictionary['operation']
        process_operation(operation, dictionary, level, result)

    result.append(f'{" " * level}}}')
    return '\n'.join(result)
