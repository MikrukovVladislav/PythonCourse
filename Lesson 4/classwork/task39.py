#  создайте модуль serializer
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


#  Cоздайте модуль deserializer. В модуле реализуйте три функции десериализации
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


#  Cоздайте пакет из двух модулей serializer и deserializer.

# Импортируйте модули пакета в отдельный файл и протестируйте все функции.
from task39_pkg import task39_serializer

task39_serializer.to_json(json.loads('{"a":"b"}'), "test_task39")
