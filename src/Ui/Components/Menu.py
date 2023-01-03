from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenuBar, QMenu, QAction, QStyle, QApplication

import webbrowser


class Menu(object):
    def __init__(self, Window: QtWidgets.QMainWindow):
        self.__Window = Window
        menuBar = QMenuBar(self.__Window)

        self.my_menu = QMenu("Menu", self.__Window)
        menuBar.addMenu(self.my_menu)

        icon = QIcon(QApplication.style().standardIcon(QStyle.SP_CommandLink))

        doc = QAction(icon, "Documentation and source code", self.__Window)
        doc.triggered.connect(self.__show_documentation)
        self.my_menu.addAction(doc)

        authors = QAction(icon, "Author", self.__Window)
        authors.triggered.connect(self.__show_author)
        self.my_menu.addAction(authors)

        self.__Window.setMenuBar(menuBar)

    def __show_author(self):
        webbrowser.open('https://www.linkedin.com/in/matsveipahotski/')

    def __show_documentation(self):
        webbrowser.open('https://github.com/MPogotsky/VoIPBandwidthCalculator')

