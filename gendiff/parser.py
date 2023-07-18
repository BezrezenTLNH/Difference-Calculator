import json
import yaml
import argparse


def parser(path):
    if path.endswith('.yml') or path.endswith('.yaml'):
        data = yaml.safe_load(open(path))

    elif path.endswith('.json'):
        data = json.load(open(path))
    return data


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
