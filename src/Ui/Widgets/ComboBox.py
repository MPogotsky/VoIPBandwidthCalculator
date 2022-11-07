from PyQt5 import QtCore, QtWidgets
from .ObjTemplate import Ui_Template

fillings = {
    "PayloadComboBox": ["G.722.1", "G.723.1", "iLBC"],
    "RTPTypesComboBox": ["RTP", "cRTP", "cRTP w/UDP"],
    "LinkHeadersComboBox": ["ethernet 802.3", "PPP"]
}

class Ui_ComboBox(Ui_Template):
    def __init__(self, group_box: QtWidgets):
        super().__init__(group_box)
        self.comboBox = None

    def setup(self, name: str, dimensions: QtCore.QSize):
        self.comboBox = QtWidgets.QComboBox(self.group_box)
        self.comboBox.setMinimumSize(dimensions)
        self.comboBox.setObjectName(name)
        self.comboBox.setFont(self.getFont())

        self._fillWithItems()

        return self.comboBox

    def _fillWithItems(self):
        filling = fillings[self.comboBox.objectName()]
        for item in filling:
            self.comboBox.addItem(item)
