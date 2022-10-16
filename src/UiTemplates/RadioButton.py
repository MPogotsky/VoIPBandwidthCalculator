from PyQt5 import QtCore, QtWidgets
from .ObjTemplate import Ui_Template


class Ui_RadioButton(Ui_Template):
    def setup(self, name: str, dimensions: QtCore.QRect):
        _button = QtWidgets.QRadioButton(self._group_box)
        _button.setGeometry(dimensions)
        _button.setFont(self.getFont())
        _button.setChecked(False)
        _button.setObjectName(name)

        return _button
