from os.path import splitext

FILE_EXTENSION = ('yaml', 'yml', 'json')


def prepare_data(filepath: str):
    extension = splitext(filepath)[1][1:]
    if extension in FILE_EXTENSION:
        with open(filepath) as f:
            data = f.read()
            return data, extension
    raise ValueError(f"Unrecognized extension: {extension}")
