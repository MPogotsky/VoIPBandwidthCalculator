from PyQt5 import QtCore, QtWidgets


class LayoutTemplate(object):
    def __init__(self, widget: QtWidgets, dimensions: QtCore.QRect, layout_name: str):
        self._main_widget = widget
        self._dimensions = dimensions
        self._layout_name = layout_name

    def setup(self, name: str):
        """Perform layout object setup"""
        pass
