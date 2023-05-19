DEFAULT_INDENT = 4


def lead_to_str(value, level: int) -> str:
    if isinstance(value, dict):
        result = ['{']
        for key, nested_value in value.items():
            if isinstance(nested_value, dict):
                new_value = lead_to_str(nested_value, level + DEFAULT_INDENT)
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


def form_string(dictionary: dict, key,
                level: int, prefix_sign: str) -> str:
    return f'{" " * level}{prefix_sign}{dictionary["key"]}: ' \
           f'{lead_to_str(dictionary[key], level + DEFAULT_INDENT)}'


def process_operation(operation: str, dictionary: dict,
                      level: int, result: list) -> None:
    if operation == 'same':
        result.append(form_string(
            dictionary, 'value',
            level, prefix_sign='    '
        ))

    if operation == 'add':
        result.append(form_string(
            dictionary, 'new',
            level, prefix_sign='  + '
        ))

    if operation == 'removed' or operation == 'changed':
        result.append(form_string(
            dictionary, 'old',
            level, prefix_sign='  - '
        ))

    if operation == 'changed':
        result.append(
            form_string(
                dictionary, 'new',
                level, prefix_sign='  + '
            ))

    if operation == 'nested':
        new_value = convert_to_stylish(dictionary['value'],
                                       level + DEFAULT_INDENT)
        result.append(f'{" " * level}    {dictionary["key"]}: {new_value}')


def convert_to_stylish(diff: dict, level=0) -> str:
    result = ['{']
    for dictionary in diff:
        operation = dictionary['operation']
        process_operation(operation, dictionary, level, result)

    result.append(f'{" " * level}}}')
    return '\n'.join(result)
