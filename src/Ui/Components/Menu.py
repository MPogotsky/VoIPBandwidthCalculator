from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenuBar, QMenu, QAction, QStyle, QApplication

import webbrowser


class Menu(object):
    def __init__(self, Window: QtWidgets.QMainWindow):
        self.__Window = Window
        menuBar = QMenuBar(self.__Window)

        menu_icon = QIcon(QApplication.style().standardIcon(QStyle.SP_MessageBoxInformation))
        self.label = menuBar.addMenu(menu_icon, "")
        self.label.setEnabled(False)

        self.help_menu = menuBar.addMenu("Help")

        sub_menu_icon = QIcon(QApplication.style().standardIcon(QStyle.SP_CommandLink))

        doc = QAction(sub_menu_icon, "Documentation and source code", self.__Window)
        doc.triggered.connect(self.__show_documentation)
        self.help_menu.addAction(doc)

        authors = QAction(sub_menu_icon, "Author", self.__Window)
        authors.triggered.connect(self.__show_author)
        self.help_menu.addAction(authors)

        self.__Window.setMenuBar(menuBar)

    def __show_author(self):
        webbrowser.open('https://www.linkedin.com/in/matsveipahotski/')

    def __show_documentation(self):
        webbrowser.open('https://github.com/MPogotsky/VoIPBandwidthCalculator')

