from gendiff.formats.stylish_formatter import convert_to_stylish
from gendiff.formats.plain_formatter import convert_to_plain
from gendiff.formats.json_formatter import convert_to_json


def get_formatter(formater):
    if formater == 'stylish':
        return convert_to_stylish
    if formater == 'plain':
        return convert_to_plain
    if formater == 'json':
        return convert_to_json
    raise ValueError(f"Unrecognized formater: {formater}")
