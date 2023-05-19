def get_operation(data1, data2, key):
    if key in data1 and key in data2:
        operation = 'changed'
    elif key in data2:
        operation = 'add'
    else:
        operation = 'removed'
    return operation


def compare_dicts(data1: dict, data2: dict) -> list[dict]:
    diff = []
    all_keys = set(data1.keys()) | set(data2.keys())
    nested_keys = set(
        k for k in all_keys if
        isinstance(data1.get(k), dict) and isinstance(data2.get(k), dict))
    for key in sorted(all_keys):
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key in nested_keys:
            child_diff = compare_dicts(value1, value2)
            if child_diff:
                diff.append({
                    'key': key,
                    'operation': 'nested',
                    'value': child_diff
                })
        elif value1 != value2:
            diff.append({
                'key': key,
                'operation': get_operation(data1, data2, key),
                'old': value1,
                'new': value2
            })
        else:
            diff.append({
                'key': key,
                'operation': 'same',
                'value': value1
            })
    return diff
