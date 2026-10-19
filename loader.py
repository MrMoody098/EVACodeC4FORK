import json


def load_raw(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
