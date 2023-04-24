import json
import pickle
import yaml


# В модуле реализуйте три функции сериализации

# Функция сериализует объект в байтовый поток pickle
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.pkl"
def to_pickle(obj, file):
    fd = open(file, "wb")
    pickle.dump(obj, fd)
    # ваш код


#  Функция сериализует объект в json
#  Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.json"
def to_json(obj, file):
    with open(file, "wt") as f:
        json.dump(obj, f, indent=4)
    # ваш код


# Функция сериализует объект в yaml
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.yml"
def to_yaml(obj, file):
    with open(file, "wt") as f:
        yaml.dump(obj, f)
    # ваш код
