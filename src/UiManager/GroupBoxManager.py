from PyQt5 import QtWidgets, QtCore

from ..UiTemplates.RadioButton import Ui_RadioButton
from ..UiTemplates.ComboBox import Ui_ComboBox
from ..UiTemplates.Label import Ui_Label
from ..UiTemplates.InputBox import Ui_InputBox


class Ui_GroupBoxManager(object):
    def __init__(self, group_box: QtWidgets.QGroupBox):
        self.radioButton = Ui_RadioButton(group_box)
        self.comboBox = Ui_ComboBox(group_box)
        self.label = Ui_Label(group_box)
        self.inputBox = Ui_InputBox(group_box)

    def setupUi(self):
        self.radioButton_payload = self.radioButton.setup("Payload", QtCore.QRect(200, 20, 131, 31))
        self.comboBox_payload = self.comboBox.setup("PayloadComboBox", QtCore.QRect(340, 21, 151, 31))

        self.label_1 = self.label.setup("label", QtCore.QRect(510, 25, 51, 21))
        self.label_2 = self.label.setup("label_2", QtCore.QRect(690, 20, 41, 31))
        self.label_3 = self.label.setup("label_3", QtCore.QRect(690, 60, 221, 31))
        self.label_4 = self.label.setup("label_4", QtCore.QRect(360, 280, 291, 31))

        self.inputBox_for_ms = self.inputBox.setup("InputForMS", QtCore.QRect(570, 20, 111, 31))
        self.inputBox_for_frames = self.inputBox.setup("InputForFrames", QtCore.QRect(570, 60, 111, 31))

        self.radioButton_RTP = self.radioButton.setup("RTP", QtCore.QRect(200, 110, 131, 31))
        self.comboBox_RTP_types = self.comboBox.setup("RTPTypesComboBox", QtCore.QRect(300, 110, 151, 31))

        self.radioButton_UDP = self.radioButton.setup("UDP", QtCore.QRect(200, 150, 131, 31))
        self.radioButton_IP = self.radioButton.setup("IP", QtCore.QRect(200, 190, 131, 31))

        self.radioButton_link = self.radioButton.setup("Link", QtCore.QRect(200, 230, 151, 31))
        self.comboBox_link_headers = self.comboBox.setup("LinkHeadersComboBox", QtCore.QRect(360, 230, 151, 31))

        self.inputBox_for_channels = self.inputBox.setup("InputForChannels", QtCore.QRect(650, 280, 111, 31))


    def raiseObjects(self):
        self.radioButton_payload.raise_()
        self.comboBox_payload.raise_()

        self.label_1.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.inputBox_for_ms.raise_()
        self.inputBox_for_frames.raise_()

        self.radioButton_RTP.raise_()
        self.comboBox_RTP_types.raise_()

        self.radioButton_UDP.raise_()
        self.radioButton_IP.raise_()

        self.radioButton_link.raise_()
        self.comboBox_link_headers.raise_()

        self.inputBox_for_channels.raise_()

    def retranslateUi(self, translate: QtCore.QCoreApplication.translate):
        self.radioButton_payload.setText(translate("MainWindow", "Payload is"))
        self.label_1.setText(translate("MainWindow", "with"))
        self.label_2.setText(translate("MainWindow", "ms"))
        self.label_3.setText(translate("MainWindow", "frames per packet"))
        self.radioButton_RTP.setText(translate("MainWindow", "RTP is"))
        self.radioButton_UDP.setText(translate("MainWindow", "UDP"))
        self.radioButton_IP.setText(translate("MainWindow", "IP"))
        self.radioButton_link.setText(translate("MainWindow", "Link header"))
        self.label_4.setText(translate("MainWindow", "For a number of channels"))
