#!/usr/bin/env python3
import argparse
from gendiff.generate_diff import generate_diff

parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
parser.add_argument('first_file', metavar='first_file', type=str)
parser.add_argument('second_file', metavar='second_file', type=str)
parser.add_argument(
    '-f', '--format', metavar='FORMAT', help='set format of output')
args = parser.parse_args()


def main():
    file1 = args.first_file
    file2 = args.second_file
    result = generate_diff(file1, file2)
    print(result)


if __name__ == '__main__':
    main()
