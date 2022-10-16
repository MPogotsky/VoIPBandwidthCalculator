from PyQt5 import QtCore, QtWidgets
from .Font import Ui_Font


class Ui_Template(object):
    def __init__(self, group_box: QtWidgets.QGroupBox):
        self._group_box = group_box
        pass

    def setup(self, name: str, dimensions: QtCore.QRect):
        """Perform ui_template object setup"""
        pass

    def getFont(self):
        """Get standard font"""
        ui_font = Ui_Font()
        font = ui_font.setup()
        return font
