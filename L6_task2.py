import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file_name) -> list[dict]:
    with open(file_name) as file:
        row_count = 0  # Переменная для выделения первой строки (шапки)
        header_list = []
        final_list = []
        for row in file:
            if row_count == 0:  # Создаем отдельно список из первой строки (шапка)
                row_clear = row.replace('\n', '')
                header_list = row_clear.split(',')
                row_count += 1
            elif row_count > 0:  # Случай для строчек с данными
                row_clear = row.replace('\n', '')
                row_list = row_clear.split(',')
                data_dict = {}
                for unit in range(len(row_list)):  # Связываем попарно значения из шапки и строки данных
                    data_dict[header_list[unit]] = row_list[unit]
                final_list.append(data_dict)
    return final_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
