from PyQt5 import QtCore, QtWidgets
from .WidgetTemplate import WidgetTemplate


class Ui_Label(WidgetTemplate):
    def setup(self, name: str, dimensions: QtCore.QSize):
        label = QtWidgets.QLabel(self._widget)
        label.setMinimumSize(dimensions)
        label.setFont(self.get_font())
        label.setObjectName(name)

        return label
