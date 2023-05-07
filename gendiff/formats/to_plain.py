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
        'add': lambda x: (f"Property '{path}{x['key']}' "
                          f"was added with value: "
                          f"{to_str(x['new'])}"),
        'removed': lambda x: (f"Property '{path}{x['key']}' was removed"),
        'nested': lambda x: build_plain_iter(x['value'], f"{path}{x['key']}."),
        'changed': lambda x: (f"Property '{path}{x['key']}' was updated. "
                              f"From {to_str(x['old'])} to "
                              f"{to_str(x['new'])}")
    }

    for dictionary in diff:
        operation = dictionary['operation']
        if operation in OPERATIONS:
            result.append(OPERATIONS[operation](dictionary))
    return '\n'.join(result)


def to_plain(diff: dict) -> str:
    return build_plain_iter(diff)
