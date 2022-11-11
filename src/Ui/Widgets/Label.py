from PyQt5 import QtCore, QtWidgets
from .ObjTemplate import Ui_Template


class Ui_Label(Ui_Template):
    def setup(self, name: str, dimensions: QtCore.QSize):
        label = QtWidgets.QLabel(self.widget)
        label.setMinimumSize(dimensions)
        label.setFont(self.getFont())
        label.setObjectName(name)

        return label
