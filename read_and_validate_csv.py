from pydantic_classes import AbatementMeasure
import csv


COLUMN_NAMES = ['name', 'net_econ_cost', 'abatement', 'category']


def read_and_validate_csv(input_filepath) -> list[AbatementMeasure]:
    validated_data = []
    with open(input_filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row_number, row in enumerate(csv_reader):
            if row_number == 0:
                validate_csv_header(row)
            else:
                validated_row = validate_abatement_row(row)
                validated_data.append(validated_row)
    return validated_data


def validate_csv_header(row: list[str]):
    if row == COLUMN_NAMES:
        return
    else:
        raise Exception('Unexpected column names detected. We expect "name", "net_econ_cost", "abatement", "category".')


def validate_abatement_row(row: list[str]):
    abatement_dict = {key: value for key, value in zip(COLUMN_NAMES, row)}
    return AbatementMeasure(**abatement_dict)