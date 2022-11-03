from PyQt5 import QtGui


class Ui_Font():
    def setup(self, font_name="Arial", size=18):
        font = QtGui.QFont()
        font.setFamily(font_name)
        font.setPointSize(size)

        return font
