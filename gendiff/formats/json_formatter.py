import json as json_global


def convert_to_json(diff) -> str:
    return json_global.dumps(diff)
