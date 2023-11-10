import csv
import typing
from typing import Optional


def read_file(path: str) -> list[list[str]]:
    '''Читает файл path и возвращает матрицу имён файлов
    Parameters
    ----------
    path(str) : Файл path
      Имя класса
    Returns
    -------
    list[list[str]]
    Матрица имён файлов'''
    files: list[list[str]] = []
    csvfile: typing.TextIO = open(path, "r")
    reader: csv.DictReader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        files.append([row["full_path"], row["class"]])
    return files


class FileIterator:
    '''Класс-итератор для получения полного пути к файлу'''
    def __init__(self, files_class: str, path: str) -> None:
        self.file_class: str = files_class
        csv_f: list[list[str]] = read_file(path)
        self.annotation: list[list[str]] = []
        for i in csv_f:
            if self.file_class == i[1]:
                self.annotation.append(i)

    def __next__(self) -> Optional[str]:
        if self.annotation:
            item_0: str = self.annotation[0][0]
            self.annotation: list[list[str]] = self.annotation[1:]
            return item_0
        else:
            return None


if __name__ == "__main__":
    path_to_annotation: str = "annotation.csv"
    fileIterator: FileIterator = FileIterator("cat", path_to_annotation)
    while True:
        next_val: Optional[str] = next(fileIterator)
        print(next_val)
        if next_val == None:
          break


