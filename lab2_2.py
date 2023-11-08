import csv
import os
import shutil
import typing


def write_file(file_name: str, data: list[list[str]]) -> None:
    '''Записывает данные в csv файл'''
    file: typing.TextIO = open(file_name, "w")
    writer: csv.writer = csv.writer(file, delimiter=",")
    for row in data:
        writer.writerow(row)
    file.close()


def copy_file(start_path: str, end_path: str) -> None:
    '''Копирует файлы'''
    dirs: list[str] = os.listdir(start_path)
    for dir in dirs:
        path: str = os.path.join(start_path, dir)
        files: list[str] = os.listdir(path)
        if not os.path.isdir(os.path.join(end_path, "dataset")):
            os.mkdir(os.path.join(end_path, "dataset"))
        for file in files:
            shutil.copyfile(os.path.join(start_path, dir, file),
                            os.path.join(end_path, "dataset", dir + "_" + file))


def create_annotation(start_path, end_path, file_name) -> None:
    '''Создаёт аннотацию'''
    data: list[list[str]] = [["full_path", "path", "class"]]

    dirs: list[str] = os.listdir(start_path)
    for dir in dirs:
        path: str = os.path.join(start_path, dir)
        files: list[str] = os.listdir(path)
        if not os.path.isdir(os.path.join(end_path, "dataset")):
            os.mkdir(os.path.join(end_path, "dataset"))

        for file in files:
            data.append([os.path.abspath(os.path.join(end_path, "dataset", dir + "_" + file)),
                         os.path.join(end_path, "dataset", dir + "_" + file), dir])
    write_file(os.path.join(end_path, file_name), data)


if __name__ == "__main__":
    start_path: str = "dataset"
    end_path: str = "my_dataset"
    file_name: str = "annotation.csv"
    copy_file(start_path, end_path)
    create_annotation(start_path, end_path, file_name)
