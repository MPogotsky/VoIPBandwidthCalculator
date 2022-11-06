from PyQt5 import QtCore, QtWidgets


class Ui_GroupBox():
    def setup(self, name: str, dimensions: QtCore.QSize, widget: QtWidgets.QWidget):
        group_box = QtWidgets.QGroupBox(widget)
        group_box.setMinimumSize(dimensions)
        group_box.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        group_box.setObjectName(name)

        return group_box
