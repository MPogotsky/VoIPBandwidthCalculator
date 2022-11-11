from PyQt5 import QtCore, QtWidgets
from .LayoutTemplate import LayoutTemplate


class Ui_GridLayout(LayoutTemplate):
    def __init__(self, widget: QtWidgets, dimensions: QtCore.QRect, layout_name: str):
        super().__init__(widget, dimensions, layout_name)

        self.widget = QtWidgets.QWidget(self._main_widget)
        self.widget.setGeometry(self._dimensions)
        self.widget.setObjectName("gridLayout")

        self.layout = QtWidgets.QGridLayout(self.widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setObjectName(self._layout_name)
