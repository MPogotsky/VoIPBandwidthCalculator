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
        self.combo_box = None

    def setup(self, name: str, dimensions: QtCore.QSize):
        self.combo_box = QtWidgets.QComboBox(self._widget)
        self.combo_box.setMinimumSize(dimensions)
        self.combo_box.setObjectName(name)
        self.combo_box.setFont(self.get_font())

        self.__fill_with_items()

        return self.combo_box

    def __fill_with_items(self):
        filling = fillings[self.combo_box.objectName()]
        for item in filling:
            self.combo_box.addItem(str(item))
