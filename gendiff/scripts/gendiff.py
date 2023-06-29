import json


def generate_diff(file_path1, file_path2):
    file_1 = json.load(open(file_path1))
    file_2 = json.load(open(file_path2))
    new_file = file_1 | file_2
    keys = sorted(new_file.keys())
    result = '{\n'

    for k in keys:
        if k in file_1 and k in file_2:
            if file_1[k] == file_2[k]:
                result += f'    {k}: {file_1[k]}\n'
            elif file_1[k] != file_2[k]:
                result += f'  - {k}: {file_1[k]}\n'
                result += f'  + {k}: {file_2[k]}\n'

        elif k in file_1 and k not in file_2:
            result += f'  - {k}: {file_1[k]}\n'

        elif k not in file_1 and k in file_2:
            result += f'  + {k}: {file_2[k]}\n'

    return str(result).lower() + '}'
