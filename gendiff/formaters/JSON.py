import json


def make_json(value):
    result = json.dumps(value, sort_keys=True, indent=4)
    return result
