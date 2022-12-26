from PyQt5 import QtCore, QtWidgets

from src.Ui.Components.Parameters import Parameters
from src.Ui.Components.Results import Results
from src.Ui.Components.InputChecks import InputChecks

from src.VoIP_Calculator.VoIP_Calculator import VoIP_Calculator
from src.VoIP_Calculator.Header import Header
from src.VoIP_Calculator.Codec import Codec


class ComponentManager(object):
    def __init__(self,
                 MainWindow: QtWidgets.QMainWindow,
                 central_widget: QtWidgets.QWidget,
                 calculator: VoIP_Calculator):
        self.__Window = MainWindow
        self.calculator = calculator
        self.validator = InputChecks(self.__Window)
        self.parameters = Parameters(self.__Window, central_widget)
        self.results = Results(self.__Window, central_widget)

        self.parameters.radio_button_payload.clicked.connect(lambda: self.__on_change())
        self.parameters.combo_box_payload.currentIndexChanged.connect(lambda: self.__on_change())

        self.parameters.input_box_for_ms.returnPressed.connect(
            lambda: [self.parameters.input_box_for_frames.setText(str("")),
                     self.__on_change()])
        self.parameters.input_box_for_frames.returnPressed.connect(
            lambda: [self.parameters.input_box_for_ms.setText(str("")),
                     self.__on_change()])

        self.parameters.input_box_for_channels.returnPressed.connect(lambda: self.__on_change())

        self.parameters.radio_button_RTP.clicked.connect(lambda: self.__on_change())
        self.parameters.radio_button_UDP.clicked.connect(lambda: self.__on_change())
        self.parameters.radio_button_IP.clicked.connect(lambda: self.__on_change())
        self.parameters.combo_box_IP_version.currentIndexChanged.connect(lambda: self.__on_change())
        self.parameters.radio_button_link.clicked.connect(lambda: self.__on_change())

    def __on_change(self):
        codec_name = str(self.parameters.combo_box_payload.currentText())
        voice_payload_size = self.parameters.input_box_for_ms.text()
        frames = self.parameters.input_box_for_frames.text()

        if voice_payload_size:
            if not self.validator.check_input_voice_payload(codec_name, voice_payload_size):
                self.parameters.input_box_for_ms.setText(str(""))
                return
            voice_payload_size = int(voice_payload_size)
            codec = Codec(codec_name, voice_payload_size=voice_payload_size)
            self.parameters.input_box_for_frames.setText(str(codec.frame_number))
        elif frames:
            if not self.validator.check_input(frames):
                self.parameters.input_box_for_frames.setText(str(""))
                return
            frames = int(frames)
            codec = Codec(codec_name, frames=frames)
            voice_payload_size = codec.voice_payload_size
            self.parameters.input_box_for_ms.setText(str(int(voice_payload_size)))
        else:
            QtWidgets.QMessageBox.information(self.__Window,
                                              "Lack of data",
                                              "Enter the number of frames or voice payload!")
            return

        channels = self.parameters.input_box_for_channels.text()
        if channels:
            if not self.validator.check_input(channels):
                self.parameters.input_box_for_channels.setText(str(""))
                return
            channels = int(channels)
        else:
            channels = 1
            self.parameters.input_box_for_channels.setText(str(channels))

        headers = []
        if self.parameters.radio_button_RTP.isChecked():
            headers.append("RTP")

        if self.parameters.radio_button_UDP.isChecked():
            headers.append("RTP")
            headers.append("UDP")

        if self.parameters.radio_button_IP.isChecked():
            headers.append("RTP")
            headers.append("UDP")
            headers.append(str(self.parameters.combo_box_IP_version.currentText()))

        if self.parameters.radio_button_link.isChecked():
            headers.append("RTP")
            headers.append("UDP")
            headers.append(str(self.parameters.combo_box_IP_version.currentText()))
            headers.append("ethernet 802.3")

        self.calculator.calculate(
            Header(headers),
            codec,
            channels)

        self.results.output_for_bandwidth.setText(str(self.calculator.get_bandwidth()))
        self.results.output_for_bandwidth.setAlignment(QtCore.Qt.AlignRight)
        self.results.output_for_packet_rate.setText(str(self.calculator.get_pps()))
        self.results.output_for_packet_rate.setAlignment(QtCore.Qt.AlignRight)

    def __set_IP_version(self):
        if self.parameters.radio_button_IP.isChecked():
            print(self.parameters.combo_box_IP_version.currentText())

    # def __check_input(self, text: str):
    #     try:
    #         int(text)
    #         if int(text) < 0:
    #             raise ValueError
    #         return True
    #     except ValueError:
    #         QtWidgets.QMessageBox.warning(self.__Window,
    #                                       "Wrong data",
    #                                       "Wrong input value! Provide positive integers!")
    #         return False
    #
    # def __check_input_voice_payload(self, text: str):
    #     try:
    #         int(text)
    #         if int(text) < 0:
    #             raise ValueError
    #         return True
    #     except ValueError:
    #         QtWidgets.QMessageBox.warning(self.__Window,
    #                                       "Wrong data",
    #                                       "Wrong input value! Provide positive integers!")
    #         return False

