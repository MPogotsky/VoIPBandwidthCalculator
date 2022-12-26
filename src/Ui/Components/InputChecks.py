from PyQt5 import QtCore, QtWidgets

from src.VoIP_Calculator.CodecSets import ITU_T_and_IETF_Defined_Codec_Interval_Standards as Codecs


class InputChecks(object):
    def __init__(self,
                 MainWindow: QtWidgets.QMainWindow):
        self.__Window = MainWindow

    def check_input(self, input_value: str) -> bool:
        try:
            int(input_value)
            if int(input_value) < 0:
                raise ValueError
            return True
        except ValueError:
            QtWidgets.QMessageBox.warning(self.__Window,
                                          "Wrong data",
                                          "Wrong input value! Provide positive integers!")
            return False

    def check_input_voice_payload(self, codec, input_value: str) -> bool:
        if not self.check_input(input_value):
            return False

        default_data = Codecs.get(codec)
        default_payload = default_data[1]
        input_value = int(input_value)

        try:
            if input_value % default_payload != 0:
                raise ValueError
            return True
        except ValueError:
            warn_text = "Wrong voice payload for codec {}, expected multiply of {} ms".format(codec, default_payload)
            QtWidgets.QMessageBox.warning(self.__Window,
                                          "Wrong data",
                                          warn_text)
            return False
