from PyQt5 import QtCore, QtWidgets


class LayoutTemplate(object):
    def __init__(self):
        self._widget = None
        self._layout = None
        pass

    def get_widget(self) -> QtWidgets.QWidget:
        return self._widget

    def get_layout(self):
        return self._layout
