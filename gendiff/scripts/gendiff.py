import argparse
import json


def gendiff():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('integers', metavar='first_file', type=str)
    parser.add_argument('integers', metavar='second_file', type=str)
    parser.add_argument('-f', '--format',
                        metavar='FORMAT', help='set format of output')
    args = parser.parse_args()


def main():
    result = generate_diff('file1.json', 'file2.json')
    print(result)


def generate_diff(file_path1, file_path2):
    file_1 = json.load(open(file_path1))
    file_2 = json.load(open(file_path2))
    new_file = file_1.copy()
    new_file.update(file_2)
    sorted_tuples = sorted(new_file.items(), key=lambda item: item[0])
    sorted_dict = {k: v for k, v in sorted_tuples}
    result = '{\n'
    for k in sorted_dict.keys():
        if k in file_1 and k in file_2:
            v_1 = str(file_1[k]).lower()
            v_2 = str(file_2[k]).lower()
            if file_1[k] == file_2[k]:
                result += f'    {k}: {v_1}\n'
            elif file_1[k] != file_2[k]:
                result += f'  - {k}: {v_1}\n'
                result += f'  + {k}: {v_2}\n'
        elif k in file_1 and k not in file_2:
            v_1 = str(file_1[k]).lower()
            result += f'  - {k}: {v_1}\n'
        elif k not in file_1 and k in file_2:
            v_2 = str(file_2[k]).lower()
            result += f'  + {k}: {v_2}\n'
    return result + '}'


if __name__ == '__main__':
    main()
