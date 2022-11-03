from PyQt5 import QtCore, QtWidgets
from .ObjTemplate import Ui_Template


class Ui_Label(Ui_Template):
    def setup(self, name: str, dimensions: QtCore.QRect):
        label = QtWidgets.QLabel(self.group_box)
        label.setGeometry(dimensions)
        label.setFont(self.getFont())
        label.setObjectName(name)

        return label
