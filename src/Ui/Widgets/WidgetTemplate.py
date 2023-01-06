from PyQt5 import QtCore, QtWidgets
from .Font import Ui_Font


class WidgetTemplate(Ui_Font, object):
    def __init__(self, widget: QtWidgets):
        super().__init__()
        self._widget = widget
        self._name = None
        self._dimensions = None

    def setup(self, name: str, dimensions: QtCore.QSize):
        """Perform ui_template object setup"""
        pass
