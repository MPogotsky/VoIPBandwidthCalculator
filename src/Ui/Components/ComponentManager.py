from PyQt5 import QtWidgets
from src.Ui.Components.Parameters import Parameters
from src.Ui.Components.Results import Results

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
        self.parameters = Parameters(self.__Window, central_widget)
        self.results = Results(self.__Window, central_widget)

        self.parameters.combo_box_payload.currentIndexChanged.connect(lambda: self.__set_codec())
        self.parameters.input_box_for_ms.returnPressed.connect(lambda: self.__set_codec())
        self.parameters.input_box_for_frames.returnPressed.connect(lambda: self.__set_codec())
        # self.parameters.combo_box_IP_version.currentIndexChanged.connect(lambda: self.__set_IP_version())
        # self.parameters.input_box_for_channels.returnPressed.connect(lambda: self.__on_click())

    def __set_codec(self):
        codec_name = str(self.parameters.combo_box_payload.currentText())
        sample_interval = self.parameters.input_box_for_ms.text()
        frames = self.parameters.input_box_for_frames.text()

        if sample_interval:
            sample_interval = int(sample_interval)
            codec = Codec(codec_name, sample_interval=sample_interval)
            self.parameters.input_box_for_frames.setText(str(codec.frame_number))
        elif frames:
            frames = int(frames)
            codec = Codec(codec_name, frames=frames)
            self.parameters.input_box_for_ms.setText(str(codec.sample_interval))
        else:
            QtWidgets.QMessageBox.information(self.__Window,
                                              "Lack of data",
                                              "Enter the number of frames or sample interval!")
            return

        channels = self.parameters.input_box_for_channels.text()
        if channels:
            channels = int(channels)
        else:
            channels = 1

        self.calculator.calculate(
                Header(),
                codec,
                channels)

        self.results.output_for_bandwidth.setText(self.calculator.get_bandwidth_as_string())
        self.results.output_for_packet_rate.setText(self.calculator.get_pps_as_string())

    def __set_IP_version(self):
        if self.parameters.radio_button_IP.isChecked():
            print(self.parameters.combo_box_IP_version.currentText())

    def __on_click(self):
        self.calculator.calculate(
            Header(["RTP", "UDP"]),
            Codec("G.711 64kbps", sample_interval=20),
            int(self.parameters.input_box_for_channels.text()))

        self.results.output_for_bandwidth.setText(self.calculator.get_bandwidth_as_string())
        self.results.output_for_packet_rate.setText(self.calculator.get_pps_as_string())