from PyQt5 import QtCore, QtWidgets
from .Font import Ui_Font


class WidgetTemplate(object):
    def __init__(self, widget: QtWidgets):
        self._widget = widget
        pass

    def setup(self, name: str, dimensions: QtCore.QSize):
        """Perform ui_template object setup"""
        pass

    def getFont(self):
        """Get standard font"""
        ui_font = Ui_Font()
        font = ui_font.setup()
        return font
