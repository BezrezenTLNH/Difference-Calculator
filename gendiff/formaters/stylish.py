import json
data = {'common': {'type': 'dictionary', 'value': None, 'children': {'follow': {'type': 'added', 'value': False, 'children': None}, 'setting1': {'type': 'untouched', 'value': 'Value 1', 'children': None}, 'setting2': {'type': 'removed', 'value': 200, 'children': None}, 'setting3': {'type': 'changed', 'value': {'old_value': True, 'new_value': None}, 'children': None}, 'setting4': {'type': 'added', 'value': 'blah blah', 'children': None}, 'setting5': {'type': 'added', 'value': {'key5': 'value5'}, 'children': None}, 'setting6': {'type': 'dictionary', 'value': None, 'children': {'doge': {'type': 'dictionary', 'value': None, 'children': {'wow': {'type': 'changed', 'value': {'old_value': '', 'new_value': 'so much'}, 'children': None}}}, 'key': {'type': 'untouched', 'value': 'value', 'children': None}, 'ops': {'type': 'added', 'value': 'vops', 'children': None}}}}}, 'group1': {'type': 'dictionary', 'value': None, 'children': {'baz': {'type': 'changed', 'value': {'old_value': 'bas', 'new_value': 'bars'}, 'children': None}, 'foo': {'type': 'untouched', 'value': 'bar', 'children': None}, 'nest': {'type': 'changed', 'value': {'old_value': {'key': 'value'}, 'new_value': 'str'}, 'children': None}}}, 'group2': {'type': 'removed', 'value': {'abc': 12345, 'deep': {'id': 45}}, 'children': None}, 'group3': {'type': 'added', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}, 'children': None}}
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


def make_stylish(object, level=0):
    result = '{\n'
    level += 1

    for k, v in object.items():
        indent = symbols['untouched'] * (level - 1)
        types = v.get('type')
        value = v.get('value')
        children = v.get('children')

        if types == 'added' or types == 'removed'\
                or types == 'untouched':
            result += f'{indent}{symbols[types]}{k}: '
            result += f'{stringify(value, level+1)}\n'

        elif types == 'changed':
            result += f'{indent}{symbols["added"]}{k}: '
            result += f'{stringify(v.get("old_value"), level + 1)}\n'
            result += f'{stringify(v.get("new_value"), level + 1)}\n'

        elif types == 'dictionary':
            result += f'{indent}{symbols["untouched"]}{k}: '
            result += f'{make_stylish(children, level)}\n'

    return result


print(make_stylish(data))
