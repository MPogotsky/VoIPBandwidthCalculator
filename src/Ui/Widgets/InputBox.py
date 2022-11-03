from PyQt5 import QtCore, QtWidgets
from .ObjTemplate import Ui_Template


class Ui_InputBox(Ui_Template):
    def setup(self, name: str, dimensions: QtCore.QRect):
        input_box = QtWidgets.QLineEdit(self.group_box)
        input_box.setGeometry(dimensions)
        input_box.setObjectName(name)
        input_box.setFont(self.getFont())
        input_box.setAlignment(QtCore.Qt.AlignRight)

        return input_box
