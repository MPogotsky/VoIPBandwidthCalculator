from PyQt5 import QtCore, QtWidgets
from .LayoutTemplate import LayoutTemplate


class Ui_HorizontalLayout(LayoutTemplate):
    def __init__(self, widget: QtWidgets, dimensions: QtCore.QRect, layout_name: str):
        super().__init__()

        self._widget = QtWidgets.QWidget(widget)
        self._widget.setGeometry(dimensions)
        self._widget.setObjectName("verticalLayout")

        self._layout = QtWidgets.QHBoxLayout(self._widget)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setObjectName(layout_name)

