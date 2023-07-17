import json
import yaml


def parser(path):
    if path.endswith('.yml') or path.endswith('.yaml'):
        data = yaml.safe_load(open(path))

    elif path.endswith('.json'):
        data = json.load(open(path))
    return data
