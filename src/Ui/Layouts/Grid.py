from PyQt5 import QtCore, QtWidgets
from .LayoutTemplate import LayoutTemplate


class Ui_GridLayout(LayoutTemplate):
    def __init__(self, widget: QtWidgets, dimensions: QtCore.QRect, layout_name: str):
        super().__init__()

        self._widget = QtWidgets.QWidget(widget)
        self._widget.setGeometry(dimensions)
        self._widget.setObjectName("gridLayout")

        self._layout = QtWidgets.QGridLayout(self._widget)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setObjectName(layout_name)
