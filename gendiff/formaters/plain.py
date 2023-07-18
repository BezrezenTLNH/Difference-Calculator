def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'

    elif value is None:
        return 'null'

    elif isinstance(value, bool):
        return 'true' if value else 'false'

    elif isinstance(value, str):
        return f"'{value}'"

    else:
        return value


def make_plain(data, path=[]):
    output = ''

    for key, value in data.items():
        types = value.get('type')
        values = value.get('value')
        children = value.get('children')
        path_copy = path.copy()
        path_copy.append(key)

        if types == 'added':
            output += f"Property '{'.'.join(path_copy)}'" \
                      f" was added with value: {get_value(values)}\n"

        elif types == 'removed':
            output += f"Property '{'.'.join(path_copy)}' was removed\n"

        elif types == 'changed':
            old = get_value(values.get('old_value'))
            new = get_value(values.get('new_value'))
            output += f"Property '{'.'.join(path_copy)}' was updated." \
                      f" From {old} to {new}\n"

        elif types == 'dictionary':
            output += f"{make_plain(children, path_copy)}\n"

    return output.strip()
