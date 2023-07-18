def create_diff(old_data, new_data):
    keys = sorted(old_data.keys() | new_data.keys())
    result = dict()

    for key in keys:
        if key not in old_data:
            result[key] = {
                'type': 'added',
                'value': new_data[key],
                'children': None
            }

        elif key not in new_data:
            result[key] = {
                'type': 'removed',
                'value': old_data[key],
                'children': None
            }

        elif old_data[key] == new_data[key]:
            result[key] = {
                'type': 'untouched',
                'value': old_data[key],
                'children': None
            }

        elif isinstance(old_data[key], dict) \
                and isinstance(new_data[key], dict):
            result[key] = {
                'type': 'dictionary',
                'value': None,
                'children': create_diff(old_data[key], new_data[key])
            }

        else:
            result[key] = {
                'type': 'changed',
                'value': {
                    'old_value': old_data[key],
                    'new_value': new_data[key]
                },
                'children': None
            }

    return result
