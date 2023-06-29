import argparse
from gendiff import generate_diff


parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', metavar='first_file', type=str)
parser.add_argument('second_file', metavar='second_file', type=str)
parser.add_argument('-f', '--format',
                        metavar='FORMAT', help='set format of output')

args = parser.parse_args()
result = generate_diff(args.first_file, args.second_file)
print(result)
