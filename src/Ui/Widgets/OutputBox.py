from PyQt5 import QtCore, QtWidgets
from .ObjTemplate import Ui_Template


class Ui_OutputBox(Ui_Template):
    def setup(self, name: str, dimensions: QtCore.QSize):
        input_box = QtWidgets.QTextBrowser(self.widget)
        input_box.setFixedSize(dimensions)
        input_box.setObjectName(name)
        input_box.setFont(self.getFont())
        input_box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        input_box.setAlignment(QtCore.Qt.AlignRight)

        return input_box
