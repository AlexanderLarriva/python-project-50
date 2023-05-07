def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, int):
        return value


def build_plain_iter(diff: dict, path="") -> str:
    result = []

    OPERATIONS = {
        'add': lambda dict: (f"Property '{path}{dict['key']}' "
                             f"was added with value: "
                             f"{to_str(dict['new'])}"),
        'removed': lambda dict: (f"Property '{path}{dict['key']}' was removed"),
        'nested': lambda dict: build_plain_iter(
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


def to_plain(diff: dict) -> str:
    return build_plain_iter(diff)
