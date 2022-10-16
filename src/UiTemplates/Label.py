from PyQt5 import QtCore, QtWidgets
from .ObjTemplate import Ui_Template


class Ui_Label(Ui_Template):
    def setup(self, name: str, dimensions: QtCore.QRect):
        _label = QtWidgets.QLabel(self._group_box)
        _label.setGeometry(dimensions)
        _label.setFont(self.getFont())
        _label.setObjectName(name)

        return _label
