def lead_to_str(value):
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


def convert_to_plain(diff: dict, path="") -> str:
    result = []

    OPERATIONS = {
        'add': lambda dict: (f"Property '{path}{dict['key']}' "
                             f"was added with value: "
                             f"{lead_to_str(dict['new'])}"),
        'removed': lambda dict: (f"Property '{path}{dict['key']}' was removed"),
        'nested': lambda dict: convert_to_plain(
            dict['value'], f"{path}{dict['key']}."),
        'changed': lambda dict: (f"Property '{path}{dict['key']}' was updated. "
                                 f"From {lead_to_str(dict['old'])} to "
                                 f"{lead_to_str(dict['new'])}")
    }

    for dictionary in diff:
        operation = dictionary['operation']
        if operation in OPERATIONS:
            result.append(OPERATIONS[operation](dictionary))
    return '\n'.join(result)
