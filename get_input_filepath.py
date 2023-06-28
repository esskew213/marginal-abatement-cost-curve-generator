from validate_filepath import validate_filepath


def get_filepath() -> str:
    input_filepath = input('Please provide the filepath to your csv file, e.g. "macc_data.csv": ')
    filepath_is_valid = validate_filepath(input_filepath)
    if filepath_is_valid:
        print(input_filepath)
        return input_filepath
    else:
        print('Invalid filepath specified. Please provide a valid filepath to a csv file.')
        return get_filepath()