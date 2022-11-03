from PyQt5 import QtCore, QtWidgets


class Ui_MenuBar(object):
    def __init__(self, Window):
        self.__Window = Window

    def setup(self, name: str, dimensions: QtCore.QRect):
        menubar = QtWidgets.QMenuBar(self.__Window)
        menubar.setGeometry(dimensions)
        menubar.setObjectName(name)

        return menubar


class Ui_SubMenu:
    def setup(self, name: str, MenuBar):
        sub_menu = QtWidgets.QMenu(MenuBar)
        sub_menu.setObjectName(name)

        return sub_menu
