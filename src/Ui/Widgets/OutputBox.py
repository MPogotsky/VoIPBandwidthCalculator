from PyQt5 import QtCore, QtWidgets
from .WidgetTemplate import WidgetTemplate


class Ui_OutputBox(WidgetTemplate):
    def setup(self, name: str, dimensions: QtCore.QSize):
        output_box = QtWidgets.QTextBrowser(self._widget)
        output_box.setFixedSize(dimensions)
        output_box.setObjectName(name)
        output_box.setFont(self.get_font())
        output_box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        output_box.setAlignment(QtCore.Qt.AlignRight)

        return output_box
