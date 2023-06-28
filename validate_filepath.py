from pathlib import Path


def validate_filepath(input_filepath: str):
    return Path(input_filepath).is_file() and input_filepath.endswith('.csv')



