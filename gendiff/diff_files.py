# import json
# import os

# def compare_dicts(dict1, dict2, key=None):
#     result = []
#     keys = set(dict1.keys()) | set(dict2.keys())
#     for k in sorted(keys):
#         if k not in dict1:
#             result.append(f"  + {key}.{k}: {dict2[k]}")
#         elif k not in dict2:
#             result.append(f"  - {key}.{k}: {dict1[k]}")
#         elif isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
#             result.extend(compare_dicts(dict1[k], dict2[k], f"{key}.{k}"))
#         elif dict1[k] != dict2[k]:
#             result.append(f"  - {key}.{k}: {dict1[k]}")
#             result.append(f"  + {key}.{k}: {dict2[k]}")
#     return result


def make_diff(file1, file2):
    diff_dict = {k: (file1.get(k), file2.get(k))
                 for k in set(file1) | set(file2)}
    result = []
    for key, values in sorted(diff_dict.items()):
        if key not in file1:
            result.append(f"  + {key}: {values[1]}")
        elif key not in file2:
            result.append(f"  - {key}: {values[0]}")
        elif key in file1 and key in file2 and file1.get(key) == file2.get(key):
            result.append(f"    {key}: {values[0]}")
        else:
            result.append(f"  - {key}: {values[0]}")
            result.append(f"  + {key}: {values[1]}")
    return "gendiff file1.json file2.json\n" \
        "{\n" + "\n".join(result) + "\n}"
