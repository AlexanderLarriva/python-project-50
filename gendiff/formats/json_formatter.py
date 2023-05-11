import json as json_global


def to_json(diff) -> str:
    return json_global.dumps(diff)
