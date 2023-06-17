import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('integers', metavar='first_file', type=str)
    parser.add_argument('integers', metavar='second_file', type=str)
    parser.add_argument('-f', '--format', metavar='FORMAT', help='set format of output')
    args = parser.parse_args()
    print(args.accamulate(args.integers))


if __name__ == '__main__':
    main()
