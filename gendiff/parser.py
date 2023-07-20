import json
import yaml
import argparse


def get_format(path):
    return path.split('.')[1]


def open_json(path):
    return json.load(open(path))


def open_yaml(path):
    return yaml.safe_load(open(path))


def parser(path):
    format = get_format(path)
    if format == 'yml' or format == 'yaml':
        return open_yaml(path)
    elif format == 'json':
        return open_json(path)
    else:
        raise Exception('This file format is supported')


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument(
        '-f', '--format', metavar='FORMAT',
        help='set format of output', default='stylish')
    args = parser.parse_args()
    return args
