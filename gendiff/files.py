from os.path import splitext

FILE_EXTENSION = ('yaml', 'yml', 'json')


def read_file(filepath: str):
    with open(filepath) as f:
        return f.read()


def prepare_data(filepath: str):
    extension = splitext(filepath)[1][1:]
    if extension in FILE_EXTENSION:
        data = read_file(filepath)
        return data, extension
    else:
        raise ValueError(f"Unrecognized extension: {extension}")
