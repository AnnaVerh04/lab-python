from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 646)
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
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setObjectName("pushButton_4")  
        self.verticalLayout.addWidget(self.pushButton_4)
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
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow","Pushbutton"))
        self.button_lab_1.setText(_translate("MainWindow", "Создание аннотации"))
        self.button_lab_2.setText(_translate("MainWindow", "Создание аннотации (class_0000.jpg)"))
        self.button_lab_3.setText(_translate("MainWindow", "Создание аннотации (random names)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Аннотации"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Обозреватель датасета"))
