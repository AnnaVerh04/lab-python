import csv
import os
import shutil
import random
import typing


def write_file(file_name: str, data: list[list[str]]) -> None:
    '''Записывает данные в csv файл
     Parameters
    ----------
    file_name(str) : Файл аннотации 
    data: (list[list[str]]): Данные '''
    file: typing.TextIO = open(file_name, "w")
    writer: csv.writer = csv.writer(file, delimiter=",")
    for row in data:
        writer.writerow(row)
    file.close()


def copy_and_create_annotation(start_path: str, end_path: str, file_name: str) -> None:
    '''Копирует и создаёт файл аннотации
    Parameters
    ----------
    start_path(str) : Стартовый путь 
    end_path:(str): Конечный путь
    file_name(str): Файл аннотации'''
    random_names: list[int] = []

    data: list[list[str]] = [["full_path", "path", "class"]]
    dirs: list[str] = os.listdir(start_path)
    for dir in dirs:
        path: str = os.path.join(start_path, dir)
        files: list[str] = os.listdir(path)
        if not os.path.isdir(os.path.join(end_path, "dataset")):
            os.mkdir(os.path.join(end_path, "dataset"))

        for file in files:

            random_file_name: int = random.randint(0, 10000)
            while random_file_name in random_names:
                random_file_name: int = random.randint(0, 10000)

            random_names.append(random_file_name)

            shutil.copyfile(os.path.join(start_path, dir, file),
                            os.path.join(end_path, "dataset", str(random_file_name) + ".jpg"))

            data.append([os.path.abspath(os.path.join(end_path, "dataset",str(random_file_name) + ".jpg")),
                         os.path.join(end_path, "dataset", str(random_file_name) + ".jpg"), dir])

    write_file(os.path.join(end_path, file_name), data)


if __name__ == "__main__":
    start_path: str = "dataset"
    end_path: str= "my_dataset2"
    file_name: str = "annotation.csv"
    copy_and_create_annotation(start_path, end_path, file_name)