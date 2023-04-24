from os.path import splitext
import json
import yaml


def parse_file(filepath):
    if splitext(filepath)[1][1:] in ('yaml', 'yml'):
        with open(filepath, 'r') as file:
            return yaml.safe_load(file)
    elif splitext(filepath)[1][1:] == 'json':
        with open(filepath, 'r') as file:
            return json.load(file)
    else:
        raise ValueError("Unsupported file format")
