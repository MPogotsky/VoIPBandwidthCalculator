from PyQt5 import QtWidgets, QtCore
from src.Ui.Widgets.MenuBar import Ui_MenuBar, Ui_SubMenu


class Ui_MenuManager(object):
    def __init__(self, Window):
        self.menu_file = None
        self.menu_bar = None
        self._Window = Window
        self.ui_menuBar = Ui_MenuBar(self._Window)
        self.ui_subMenu = Ui_SubMenu()

    def setupUi(self):
        self.menu_bar = self.ui_menuBar.setup("MenuBar", QtCore.QRect(0, 0, 1134, 21))
        self.menu_file = self.ui_subMenu.setup("File", self.menu_bar)

        self._Window.setMenuBar(self.menu_bar)

        status_bar = QtWidgets.QStatusBar(self._Window)
        status_bar.setObjectName("statusbar")
        self._Window.setStatusBar(status_bar)
        self.menu_bar.addAction(self.menu_file.menuAction())

    def retranslateUi(self, translate: QtCore.QCoreApplication.translate):
        self.menu_file.setTitle(translate("MainWindow", "File"))
