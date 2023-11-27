import os
import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QFileSystemModel

from form import Ui_MainWindow
import Creating_a_annotations, Copying_a_dataset, Copying_with_a_random_number, Iterator_class


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.cat_iterator = None
        self.dog_iterator = None
        self.path_to_tree = None
        self.dirModel = None

        self.ui.button_lab_1.clicked.connect(self.click_button_lab_1)
        self.ui.button_lab_2.clicked.connect(self.click_button_lab_2)
        self.ui.button_lab_3.clicked.connect(self.click_button_lab_3)
        self.ui.button_tree.clicked.connect(self.click_button_tree)

        self.ui.button_next_cat.clicked.connect(self.click_next_cat)
        self.ui.button_next_dog.clicked.connect(self.click_next_dog)
        self.ui.button_get_annotation.clicked.connect(self.click_get_annotation)


    '''Функционал кнопки для пролистывания котов
    Parameters
    ----------
    self: Новый объект
    '''
    def click_next_cat(self):
        path = next(self.cat_iterator)
        self.resize_image(path)

    '''Функционал кнопки для пролистывания собак
    Parameters
    ----------
    self: Новый объект
    '''

    def click_next_dog(self):
        path = next(self.dog_iterator)
        self.resize_image(path)

    '''Функция для масштабирования картинок
    Parameters
    ----------
    self: Новый объект
    path: Путь
    '''

    def resize_image(self, path):
        pixmap = QPixmap(path)
        if pixmap.width() > pixmap.height():
            pixmap = pixmap.scaledToWidth(self.ui.image.width())
        else:
            pixmap = pixmap.scaledToHeight(self.ui.image.height())
        self.ui.image.setPixmap(pixmap)

    '''Функционал для получения аннотации
    Parameters
    ----------
    self: Новый объект
    '''

    def click_get_annotation(self):
        filter = "csv(*.csv)"
        path = QFileDialog.getOpenFileName(filter=filter)
        self.cat_iterator = Iterator_class.FileIterator("cat", path[0])
        self.dog_iterator = Iterator_class.FileIterator("dog", path[0])

    '''Функционал для создания аннотации
    Parameters
    ----------
    self: Новый объект
    '''

    def click_button_lab_1(self):
        path = QFileDialog.getExistingDirectory(self, "Путь к dataset")
        path_to_annotation: str = "annotation.csv"
        print(os.path.relpath(path))
        Creating_a_annotations.create_annotation(os.path.relpath(path), path_to_annotation)

    '''Функционал копирования аннотации и dataset 
    Parameters
    ----------
    self: Новый объект
    '''
    def click_button_lab_2(self):
        start_path = QFileDialog.getExistingDirectory(self, "Путь к dataset")
        end_path = QFileDialog.getExistingDirectory(self, "Новое расположение")

        file_name: str = "annotation.csv"
        Copying_a_dataset.copy_file(start_path, end_path)
        Copying_a_dataset.create_annotation(os.path.relpath(start_path), os.path.relpath(end_path), file_name)

    '''Функционал копирования аннотации и dataset с рандомными номерами
    Parameters
    ----------
    self: Новый объект
    '''
    def click_button_lab_3(self):
        start_path = QFileDialog.getExistingDirectory(self, "Путь к dataset")
        end_path = QFileDialog.getExistingDirectory(self, "Новое расположение")

        file_name: str = "annotation.csv"
        Copying_with_a_random_number.copy_and_create_annotation(os.path.relpath(start_path), os.path.relpath(end_path), file_name)

    '''Функционал создания дерева файлов
    Parameters
    ----------
    self: Новый объект
    '''
    def click_button_tree(self):
        self.path_to_tree = QFileDialog.getExistingDirectory()
        self.dirModel = QFileSystemModel(self)
        self.dirModel.setRootPath(self.path_to_tree)
        self.ui.treeView.setModel(self.dirModel)
        self.ui.treeView.setRootIndex(self.dirModel.index(self.path_to_tree))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
