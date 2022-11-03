from PyQt5 import QtCore, QtWidgets
from .ObjTemplate import Ui_Template


class Ui_RadioButton(Ui_Template):
    def setup(self, name: str, dimensions: QtCore.QRect):
        button = QtWidgets.QRadioButton(self.group_box)
        button.setGeometry(dimensions)
        button.setFont(self.getFont())
        button.setChecked(False)
        button.setObjectName(name)

        return button
