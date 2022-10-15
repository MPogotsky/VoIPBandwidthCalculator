from PyQt5 import QtCore, QtWidgets


class Ui_GroupBox(object):
    def setup(self, name: str, dimensions: QtCore.QRect, widget: QtWidgets.QWidget):
        groupBox = QtWidgets.QGroupBox(widget)
        groupBox.setGeometry(dimensions)
        groupBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        groupBox.setObjectName(name)

        return groupBox
