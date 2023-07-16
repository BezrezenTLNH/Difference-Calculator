#!/usr/bin/env python3
import argparse
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


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument(
        '-f', '--format', metavar='FORMAT',
        help='set format of output', default='stylish')
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


if __name__ == '__main__':
    main()
