import json


symbols = {
    'added': '  + ',
    'removed': '  - ',
    'untouched': '    '
}


def stringify(value, level=1):
    result = '{\n'
    indent = "    "

    if isinstance(value, str):
        return value

    if isinstance(value, bool):
        return 'true' if value else 'false'

    if isinstance(value, dict):
        for k, v in value.items():
            result += f'{indent*level}{k}: '
            result += f'{stringify(v, level + 1)}\n'
        result += f'{indent*(level - 1)}}}'

        return result

    else:
        return json.dumps(value)


def make_stylish(object_dict, level=0):
    result = '{\n'
    level += 1

    for k, v in object_dict.items():
        indent = symbols['untouched'] * (level - 1)
        types = v.get('type')
        value = v.get('value')
        children = v.get('children')

        if types == 'added' or types == 'removed'\
                or types == 'untouched':
            result += f'{indent}{symbols[types]}{k}: '
            result += f'{stringify(value, level+1)}\n'

        elif types == 'changed':
            result += f'{indent}{symbols["removed"]}{k}: '
            result += f'{stringify(value.get("old_value"), level + 1)}\n'
            result += f'{indent}{symbols["added"]}{k}: '
            result += f'{stringify(value.get("new_value"), level + 1)}\n'

        elif types == 'dictionary':
            result += f'{indent}{symbols["untouched"]}{k}: '
            result += f'{make_stylish(children, level)}\n'
    result += f'{indent}}}'
    return result
