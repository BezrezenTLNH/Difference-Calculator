from gendiff.parser import parser
from gendiff.get_diff import get_diff


def generate_diff(file_path1, file_path2):
    data1 = parser(file_path1)
    data2 = parser(file_path2)
    new_file = data1 | data2
    keys = sorted(new_file.keys())
    result = '{\n'

    for k in keys:
        if k in data1 and k in data2:
            if data1[k] == data2[k]:
                result += f'    {k}: {data1[k]}\n'
            elif data1[k] != data2[k]:
                result += f'  - {k}: {data1[k]}\n'
                result += f'  + {k}: {data2[k]}\n'

        elif k in data1 and k not in data2:
            result += f'  - {k}: {data1[k]}\n'

        elif k not in data1 and k in data2:
            result += f'  + {k}: {data2[k]}\n'

    return str(result).lower() + '}'

