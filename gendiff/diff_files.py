def make_diff(dict1, dict2):
    diff_dict = {k: (dict1.get(k), dict2.get(k))
                 for k in set(dict1) | set(dict2)}
    result = []
    for key, values in sorted(diff_dict.items()):
        if key not in dict1:
            result.append(f"  + {key}: {values[1]}")
        elif key not in dict2:
            result.append(f"  - {key}: {values[0]}")
        elif key in dict1 and key in dict2 and dict1.get(key) == dict2.get(key):
            result.append(f"    {key}: {values[0]}")
        else:
            result.append(f"  - {key}: {values[0]}")
            result.append(f"  + {key}: {values[1]}")
    # возврат дифа
    return ("{\n" + "\n".join(result) + "\n}")
