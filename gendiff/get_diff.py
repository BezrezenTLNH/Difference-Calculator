def create_and_get_diff(old_data, new_data):
    keys = sorted(old_data.keys() | new_data.keys())
    result = dict()

    for k in keys:
        if k not in old_data:
            result[k] = {
                'type': 'added',
                'value': new_data[k],
                'children': None
            }

        elif k not in new_data:
            result[k] = {
                'type': 'removed',
                'value': old_data[k],
                'children': None
            }

        elif old_data[k] == new_data[k]:
            result[k] = {
                'type': 'untouched',
                'value': old_data[k],
                'children': None
            }

        elif isinstance(old_data[k], dict) and isinstance(new_data[k], dict):
            result[k] = {
                'type': 'dictionary',
                'value': None,
                'children': create_and_get_diff(old_data[k], new_data[k])
            }

        else:
            result[k] = {
                'type': 'changed',
                'value': {
                    'old_value': old_data[k],
                    'new_value': new_data[k]
                },
                'children': None
            }

    return result
