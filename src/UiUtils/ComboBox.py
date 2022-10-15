from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_ComboBox(object):
    def setup(self, name: str, dimensions: QtCore.QRect, groupBox: QtWidgets.QGroupBox):
        comboBox = QtWidgets.QComboBox(groupBox)
        comboBox.setGeometry(dimensions)
        comboBox.setObjectName(name)

        return comboBox