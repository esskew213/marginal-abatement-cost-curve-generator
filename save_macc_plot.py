from ask_yes_or_no import ask_yes_or_no


SUPPORTED_FORMATS = ['png', 'pdf', 'svg', 'jpg']


def save_macc_plot(macc_plot) -> None:
    user_wants_to_save = ask_yes_or_no('Do you want to save a copy of this MAC curve?')
    if not user_wants_to_save:
        print('MAC curve not saved.')
        return
    else:
        user_file_name = input('Provide a file name (no special characters): ')
        validated_file_name = validate_file_name(user_file_name)
        output_format = get_output_format()
        macc_plot.savefig(f'{validated_file_name}.{output_format}', dpi=400)
        print('MAC curve saved.')
        return


def validate_file_name(user_file_name):
    return user_file_name


def get_output_format():
    user_output_format = input(f'Indicate your desired file extension: ' + ", ".join([f"{x}" for x in SUPPORTED_FORMATS]) + ": ")
    if user_output_format.lower() in SUPPORTED_FORMATS:
        return user_output_format
    else:
        print(f'Invalid image extension. Please indicate one of the following: ' + ", ".join([f"{x}" for x in SUPPORTED_FORMATS]))
        return get_output_format()

