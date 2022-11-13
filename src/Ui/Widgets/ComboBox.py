from PyQt5 import QtCore, QtWidgets
from .WidgetTemplate import WidgetTemplate

from src.VoIP_Calculator.CodecSets import ITU_T_and_IETF_Defined_Codec_Interval_Standards
fillings = {
    "PayloadComboBox": list(ITU_T_and_IETF_Defined_Codec_Interval_Standards.keys()),
    "IPVersionComboBox": ["IPv4", "IPv6"]
}

class Ui_ComboBox(WidgetTemplate):
    def __init__(self, group_box: QtWidgets):
        super().__init__(group_box)
        self.comboBox = None

    def setup(self, name: str, dimensions: QtCore.QSize):
        self.comboBox = QtWidgets.QComboBox(self._widget)
        self.comboBox.setMinimumSize(dimensions)
        self.comboBox.setObjectName(name)
        self.comboBox.setFont(self.getFont())

        self._fillWithItems()

        return self.comboBox

    def _fillWithItems(self):
        filling = fillings[self.comboBox.objectName()]
        for item in filling:
            self.comboBox.addItem(item)
