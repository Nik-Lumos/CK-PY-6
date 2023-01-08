import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file_name) -> list[dict]:
    with open(file_name) as file:
        header_str = file.readline()
        header_list = header_str.replace('\n', '').split(',')
        final = [dict(zip(header_list, row.replace('\n', '').split(','))) for row in file]

    return final


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
