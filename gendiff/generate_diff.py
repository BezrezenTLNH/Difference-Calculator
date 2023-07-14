from gendiff.parser import parser
from gendiff.get_diff import create_and_get_diff
from gendiff.formaters.stylish import make_stylish
from gendiff.formaters.plain import make_plain
from gendiff.formaters.JSON import make_json


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parser(file_path1)
    data2 = parser(file_path2)
    formatted_data = create_and_get_diff(data1, data2)
    if format_name == 'plain':
        return make_plain(formatted_data)
    elif format_name == 'json':
        return make_json(formatted_data)
    else:
        return make_stylish(formatted_data)
    raise Exception(f"You chose the wrong format!: {format}")
