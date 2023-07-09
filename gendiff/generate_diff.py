from gendiff.parser import parser
from gendiff.get_diff import create_and_get_diff
from gendiff.formaters.stylish import make_stylish


def generate_diff(file_path1, file_path2, format='stylish'):
    data1 = parser(file_path1)
    data2 = parser(file_path2)
    formatted_data = create_and_get_diff(data1, data2)
    return make_stylish(formatted_data)
