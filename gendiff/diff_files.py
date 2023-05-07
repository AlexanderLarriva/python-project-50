def make_diff(data1: dict, data2: dict) -> list:
    diff = []
    all_keys = set(data1.keys()) | set(data2.keys())
    nested_keys = set(
        k for k in all_keys if
        isinstance(data1.get(k), dict) and isinstance(data2.get(k), dict))
    for key in sorted(all_keys):
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key in nested_keys:
            child_diff = make_diff(value1, value2)
            if child_diff:
                diff.append({
                    'key': key, 'operation': 'nested', 'value': child_diff
                })
        elif value1 != value2:
            operation = 'changed' if key in data1 and key in data2 \
                else 'add' if key in data2 else 'removed'
            diff.append({
                'key': key, 'operation': operation, 'old': value1, 'new': value2
            })
        else:
            diff.append({
                'key': key, 'operation': 'same', 'value': value1
            })
    return diff
