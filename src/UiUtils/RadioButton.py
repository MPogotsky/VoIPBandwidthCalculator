from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_RadioButton(object):
    def setup(self, name: str, dimensions: QtCore.QRect, groupBox: QtWidgets.QGroupBox):
        button = QtWidgets.QRadioButton(groupBox)
        button.setGeometry(dimensions)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        button.setFont(font)
        button.setChecked(False)
        button.setObjectName(name)

        return button
