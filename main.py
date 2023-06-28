from read_and_validate_csv import read_and_validate_csv
from get_macc_plot import get_macc_plot
from save_macc_plot import save_macc_plot
from get_input_filepath import get_filepath
from macc_transforms import macc_transforms
from ask_yes_or_no import ask_yes_or_no


def get_and_save_macc_from_csv() -> None:
    input_filepath = get_filepath()
    validated_data = read_and_validate_csv(input_filepath)
    macc_input_data = macc_transforms(validated_data)
    # save_transformed_csv(macc_input_data)
    macc_plot = get_macc_plot(macc_input_data)
    save_macc_plot(macc_plot)
    rerun_generator = ask_yes_or_no('Do you want to create another MAC curve?')
    if not rerun_generator:
        pass
    else:
        return get_and_save_macc_from_csv()
    print('Exiting application. Thank you for using the MAC curve generator!')


if __name__ == '__main__':
    get_and_save_macc_from_csv()