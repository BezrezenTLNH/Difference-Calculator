from gendiff.formaters.stylish import make_stylish
from gendiff.formaters.plain import make_plain
from gendiff.formaters.json import make_json


def format_checker(format_name, formatted_data):
    if format_name == 'plain':
        return make_plain(formatted_data)
    elif format_name == 'json':
        return make_json(formatted_data)
    else:
        return make_stylish(formatted_data)
