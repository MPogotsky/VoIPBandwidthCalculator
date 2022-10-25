from PyQt5 import QtGui


class Ui_Font():
    def setup(self, type="Arial", size=18):
        font = QtGui.QFont()
        font.setFamily(type)
        font.setPointSize(size)

        return font