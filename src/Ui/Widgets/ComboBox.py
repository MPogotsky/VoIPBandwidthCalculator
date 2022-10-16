from PyQt5 import QtCore, QtWidgets
from .ObjTemplate import Ui_Template


class Ui_ComboBox(Ui_Template):
    def setup(self, name: str, dimensions: QtCore.QRect):
        _comboBox = QtWidgets.QComboBox(self._group_box)
        _comboBox.setGeometry(dimensions)
        _comboBox.setObjectName(name)

        return _comboBox
