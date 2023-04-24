# Функция десериализует объект из файла типа pickle
# file - файл для десериализации к примеру "data.pkl"
import json
import pickle

import yaml


def from_pickle(file):
    with open(file, "rb") as f:
        obj = pickle.load(f)
    return obj
    # ваш код


# Функция десериализует объект из файла типа json
# from_json - функция сереализует объект в json
# Параметры
# file - файл для десериализации к примеру "data.json"
def from_json(file):
    with open(file, "rt") as f:
        obj = json.load(f)
    return obj
    # ваш код


# Функция десериализует объект из файла типа yaml
# Параметры
# file - файл для десериализации к примеру "data.yml"
def from_yaml(file):
    with open(file, "wt") as f:
        obj = yaml.load(f)
    return obj
    # ваш код
