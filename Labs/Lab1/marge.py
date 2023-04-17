import os
from argparse import ArgumentParser

import logging


def find_files(catalog):
    find_files = []
    for root, dirs, files in os.walk(catalog):
        find_files += [os.path.join(root, name) for name in files]
    return find_files


parser = ArgumentParser(prog="argparse_simple", description="Программа для знакомства с библ. argparse.",
                        epilog="Приятного пользования!")
parser.add_argument('output', help="выходной файл")  # positional argument
parser.add_argument("--root_dir", help="Принимает папку для обработки")

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.name = "Marge.py"
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s %(name)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    args = parser.parse_args()

    logger.info("Scan dirs")
    data = dict()
    data["VectorTelemetry"] = dict()
    logger.info("Read files")
    for filename in find_files(args.root_dir):
        with open(filename, 'r') as f:
            data["VectorTelemetry"][str(filename).split("\\")[-1]] = float(f.read())

    logger.info("Write result")
    with open(args.output, 'w+') as f:
        f.write(str(data).replace('\"', '').replace('\'', '\"'))

    logger.info("End...")
