from PyQt5 import QtCore, QtWidgets
from .ObjTemplate import Ui_Template


class Ui_InputBox(Ui_Template):
    def setup(self, name: str, dimensions: QtCore.QRect):
        _input_box = QtWidgets.QLineEdit(self._group_box)
        _input_box.setGeometry(dimensions)
        _input_box.setObjectName(name)
        _input_box.setFont(self.getFont())
        _input_box.setAlignment(QtCore.Qt.AlignRight)

        return _input_box
