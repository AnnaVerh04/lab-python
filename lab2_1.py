import csv
import os
import typing


def write_file(file_name: str, data: list[list[str]]) -> None:
    '''Записывает данные в csv файл'''
    file: typing.TextIO = open(file_name, "w")
    writer: csv.writer = csv.writer(file, delimiter=",")
    for row in data:
        writer.writerow(row)
    file.close()


def create_annotation(path_data: str, path_to_annotation: str) -> None:
    '''Создаёт аннотацию'''
    data: list[list[str]] = [["full_path", "path", "class"]]

    dirs: list[str] = os.listdir(path_data)

    for dir in dirs:
        path: str = os.path.join(path_data, dir)
        files: list[str] = os.listdir(path)
        for file in files:
            data.append([os.path.abspath(os.path.join(path, file)),
                         os.path.join(path, file),
                         dir])

    write_file(file_name=path_to_annotation, data=data)


if __name__ == "__main__":
    path_to_annotation: str = "annotation.csv"
    path_data: str = "dataset"
    create_annotation(path_data, path_to_annotation)
