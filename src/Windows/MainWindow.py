from PyQt5 import QtCore
from src.Ui.Components.GroupBoxManager import GroupBoxManager
from src.Ui.Components.Menu import Menu


class Ui_MainWindow(object):
    def __init__(self):
        self.parameters = None
        self.upper_menu = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        self.upper_menu = Menu(MainWindow)
        self.group_boxes = GroupBoxManager(MainWindow)

        self.upper_menu.setupUi()
        self.group_boxes.setupUi()

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.upper_menu.retranslateUi(_translate)
        self.group_boxes.retranslateUi(_translate)
