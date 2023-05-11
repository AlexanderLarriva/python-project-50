from gendiff.formats.stylish_formatter import to_stylish
from gendiff.formats.plain_formatter import to_plain
from gendiff.formats.json_formatter import to_json


def get_formatter(formater):
    if formater == 'stylish':
        return to_stylish
    if formater == 'plain':
        return to_plain
    if formater == 'json':
        return to_json
    raise ValueError(f"Unrecognized formater: {formater}")
