from parser import parser
data1 = parser('tests/fixtures/file1_stylish.json')
data2 = parser('tests/fixtures/file2_stylish.json')

def create_and_get_diff(old_data, new_data):
    keys = sorted(old_data.keys() | new_data.keys())
    result = dict()

    for k in keys:
        if k not in old_data:
            result[k] = {
                'type': 'added',
                'value': str(new_data[k]).lower(),
                'children': None
            }
        elif k not in new_data:
            result[k] = {
                'type': 'removed',
                'value': str(old_data[k]).lower(),
                'children': None
            }
        elif old_data[k] == new_data[k]:
            result[k] = {
                'type': 'untouched',
                'value': str(old_data[k]).lower(),
                'children': None
            }
        elif isinstance(old_data[k], dict) and isinstance(new_data[k], dict):
            result[k] = {
                'type': 'dictionary',
                'value': old_data[k],
                'children': create_and_get_diff(old_data[k], new_data[k])
            }
        else:
            result[k] = {
                'type': 'changed',
                'value': {
                    'old_value': str(old_data[k]).lower(),
                    'new_value': str(new_data[k]).lower()
                },
                'children': None
            }
    return result


print(create_and_get_diff(data1, data2))
