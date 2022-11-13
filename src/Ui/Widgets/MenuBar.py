from PyQt5 import QtCore, QtWidgets


class Ui_MenuBar(object):
    def __init__(self, Window):
        self.__Window = Window

    def setup(self, name: str, dimensions: QtCore.QRect):
        menu_bar = QtWidgets.QMenuBar(self.__Window)
        menu_bar.setGeometry(dimensions)
        menu_bar.setObjectName(name)

        return menu_bar


class Ui_SubMenu:
    def setup(self, name: str, MenuBar):
        sub_menu = QtWidgets.QMenu(MenuBar)
        sub_menu.setObjectName(name)

        return sub_menu
