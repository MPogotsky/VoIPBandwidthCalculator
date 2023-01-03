from PyQt5 import QtCore, QtWidgets
from .WidgetTemplate import WidgetTemplate


class Ui_RadioButton(WidgetTemplate):
    def setup(self, name: str, dimensions: QtCore.QSize):
        button = QtWidgets.QRadioButton(self._widget)
        button.setMinimumSize(dimensions)
        button.setFont(self.font)
        button.setChecked(False)
        button.setObjectName(name)

        return button
