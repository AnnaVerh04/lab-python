import os
import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog

from form import Ui_MainWindow
import Creating_a_annotations, Copying_a_dataset, Copying_with_a_random_number, Iterator_class




class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_lab_1.clicked.connect(self.click_button_lab_1)
        self.ui.button_lab_2.clicked.connect(self.click_button_lab_2)
        self.ui.button_lab_3.clicked.connect(self.click_button_lab_3)

    
    def click_button_lab_1(self):
        path = QFileDialog.getExistingDirectory(self, "Путь к dataset")
        path_to_annotation: str = "annotation.csv"
        print(os.path.relpath(path))
        Creating_a_annotations.create_annotation(os.path.relpath(path), path_to_annotation)

    
    def click_button_lab_2(self):
        start_path = QFileDialog.getExistingDirectory(self, "Путь к dataset")
        end_path = QFileDialog.getExistingDirectory(self, "Новое расположение")

        file_name: str = "annotation.csv"
        Copying_a_dataset.copy_file(start_path, end_path)
        Copying_a_dataset.create_annotation(os.path.relpath(start_path), os.path.relpath(end_path), file_name)


    def click_button_lab_3(self):
        start_path = QFileDialog.getExistingDirectory(self, "Путь к dataset")
        end_path = QFileDialog.getExistingDirectory(self, "Новое расположение")

        file_name: str = "annotation.csv"
        Copying_with_a_random_number.copy_and_create_annotation(os.path.relpath(start_path), os.path.relpath(end_path), file_name)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
