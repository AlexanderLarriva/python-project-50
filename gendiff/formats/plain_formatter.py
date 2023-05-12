def to_str(value):
    value_check = {
        dict: "[complex value]",
        bool: str(value).lower(),
        type(None): "null",
        int: str(value)
    }
    for key in value_check:
        if isinstance(value, key):
            return value_check[key]
    return f"'{value}'"


def to_plain(diff: dict, path="") -> str:
    result = []

    OPERATIONS = {
        'add': lambda dict: (f"Property '{path}{dict['key']}' "
                             f"was added with value: "
                             f"{to_str(dict['new'])}"),
        'removed': lambda dict: (f"Property '{path}{dict['key']}' was removed"),
        'nested': lambda dict: to_plain(
            dict['value'], f"{path}{dict['key']}."),
        'changed': lambda dict: (f"Property '{path}{dict['key']}' was updated. "
                                 f"From {to_str(dict['old'])} to "
                                 f"{to_str(dict['new'])}")
    }

    for dictionary in diff:
        operation = dictionary['operation']
        if operation in OPERATIONS:
            result.append(OPERATIONS[operation](dictionary))
    return '\n'.join(result)
