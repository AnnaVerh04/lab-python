from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 561)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_tree = QtWidgets.QPushButton(self.tab)
        self.button_tree.setObjectName("button_tree")
        self.verticalLayout.addWidget(self.button_tree)
        self.treeView = QtWidgets.QTreeView(self.tab)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_lab_1 = QtWidgets.QPushButton(self.tab)
        self.button_lab_1.setObjectName("button_lab_1")
        self.horizontalLayout.addWidget(self.button_lab_1)
        self.button_lab_2 = QtWidgets.QPushButton(self.tab)
        self.button_lab_2.setObjectName("button_lab_2")
        self.horizontalLayout.addWidget(self.button_lab_2)
        self.button_lab_3 = QtWidgets.QPushButton(self.tab)
        self.button_lab_3.setObjectName("button_lab_3")
        self.horizontalLayout.addWidget(self.button_lab_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.image = QtWidgets.QLabel(self.tab_2)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.verticalLayout_2.addWidget(self.image)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_next_cat = QtWidgets.QPushButton(self.tab_2)
        self.button_next_cat.setObjectName("button_next_cat")
        self.horizontalLayout_2.addWidget(self.button_next_cat)
        self.button_get_annotation = QtWidgets.QPushButton(self.tab_2)
        self.button_get_annotation.setObjectName("button_get_annotation")
        self.horizontalLayout_2.addWidget(self.button_get_annotation)
        self.button_next_dog = QtWidgets.QPushButton(self.tab_2)
        self.button_next_dog.setObjectName("button_next_dog")
        self.horizontalLayout_2.addWidget(self.button_next_dog)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_tree.setText(_translate("MainWindow", "Отобразить дирректорию"))
        self.button_lab_1.setText(_translate("MainWindow", "Создание аннотации"))
        self.button_lab_2.setText(_translate("MainWindow", "Копирование датасета (class_0000.jpg)"))
        self.button_lab_3.setText(_translate("MainWindow", "Копирование датасета (random names)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Аннотации"))
        self.image.setText(_translate("MainWindow", "TextLabel"))
        self.button_next_cat.setText(_translate("MainWindow", "Следующий кот"))
        self.button_get_annotation.setText(_translate("MainWindow", "Открыть dataset"))
        self.button_next_dog.setText(_translate("MainWindow", "Следующий пёс"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Обозреватель датасета"))
