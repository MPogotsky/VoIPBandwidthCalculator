from PyQt5 import QtCore, QtWidgets
from .WidgetTemplate import WidgetTemplate


class Ui_InputBox(WidgetTemplate):
    def setup(self, name: str, dimensions: QtCore.QSize):
        input_box = QtWidgets.QLineEdit(self._widget)
        input_box.setMinimumSize(dimensions)
        input_box.setObjectName(name)
        input_box.setFont(self.font)
        input_box.setAlignment(QtCore.Qt.AlignRight)

        return input_box
