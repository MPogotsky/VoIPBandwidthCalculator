from PyQt5 import QtCore, QtWidgets


class Ui_MenuBar(object):
    def __init__(self, Window):
        self._Window = Window

    def setup(self, name: str, dimensions: QtCore.QRect):
        _menubar = QtWidgets.QMenuBar(self._Window)
        _menubar.setGeometry(dimensions)
        _menubar.setObjectName(name)

        return _menubar


class Ui_SubMenu:
    def setup(self, name: str, MenuBar):
        _subMenu = QtWidgets.QMenu(MenuBar)
        _subMenu.setObjectName(name)

        return _subMenu
