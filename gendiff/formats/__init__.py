from gendiff.formats.to_stylish import to_stylish
from gendiff.formats.to_plain import to_plain
from gendiff.formats.to_json import to_json


def get_formatter(formater):
    if formater == 'stylish':
        return to_stylish
    if formater == 'plain':
        return to_plain
    if formater == 'json':
        return to_json
    raise ValueError(f"Unrecognized formater: {formater}")
