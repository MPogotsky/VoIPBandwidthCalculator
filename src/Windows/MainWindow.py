from PyQt5 import QtCore, QtWidgets
from src.Ui.Widgets.GroupBox import Ui_GroupBox
from src.Ui.Managers.GroupBoxManager import Ui_GroupBoxManager
from src.Ui.Managers.MenuManager import Ui_MenuManager

class Ui_MainWindow(object):
    def __init__(self):
        self.ui_groupBoxManager = None
        self.ui_menuManager = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1134, 755)

        self.ui_menuManager = Ui_MenuManager(MainWindow)
        self.ui_groupBoxManager = Ui_GroupBoxManager(MainWindow)

        self.ui_menuManager.setupUi()
        self.ui_groupBoxManager.setupUi()

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.ui_groupBoxManager.retranslateUi(_translate)
        self.ui_menuManager.retranslateUi(_translate)
