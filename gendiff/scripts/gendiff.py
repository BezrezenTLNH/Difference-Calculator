#!/usr/bin/env python3
import argparse
from gendiff.generate_diff import generate_diff


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