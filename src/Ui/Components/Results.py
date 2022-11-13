from PyQt5 import QtCore, QtWidgets

from src.Ui.Layouts.Horizontal import Ui_HorizontalLayout
from src.Ui.Widgets.GroupBox import Ui_GroupBox
from src.Ui.Widgets.Label import Ui_Label
from src.Ui.Widgets.OutputBox import Ui_OutputBox


class Results(object):
    def __init__(self, Window: QtWidgets.QMainWindow, widget: QtWidgets.QWidget):
        self.__Window = Window
        self.__central_widget = widget

        GroupBox = Ui_GroupBox()
        self.__group_box = GroupBox.setup("Result",
                                          QtCore.QRect(9, 420, 1160, 340),
                                          self.__central_widget)
        self.__setup_dependencies()

    def __setup_dependencies(self):
        self.__setup_bandwidth()
        self.__setup_packet_rate()
        self.__retranslate_Ui()

    def __setup_bandwidth(self):
        bandwidth_horizontal = Ui_HorizontalLayout(self.__group_box,
                                                   QtCore.QRect(350, 100, 400, 50),
                                                   "ResultLayout")

        Label = Ui_Label(bandwidth_horizontal.widget)
        OutputBox = Ui_OutputBox(bandwidth_horizontal.widget)

        bandwidth_horizontal.layout.setAlignment(QtCore.Qt.AlignLeft)
        bandwidth_horizontal.layout.addStretch(1)

        self.label_5 = Label.setup("label_5", QtCore.QSize(100, 31))
        bandwidth_horizontal.layout.addWidget(self.label_5)
        bandwidth_horizontal.layout.addSpacing(5)

        self.output_for_bandwidth = OutputBox.setup("OutForBandwidth", QtCore.QSize(100, 31))
        bandwidth_horizontal.layout.setAlignment(QtCore.Qt.AlignLeft)
        bandwidth_horizontal.layout.addWidget(self.output_for_bandwidth)

        self.label_6 = Label.setup("label_6", QtCore.QSize(60, 31))
        bandwidth_horizontal.layout.addWidget(self.label_6)

    def __setup_packet_rate(self):
        packet_rate_horizontal = Ui_HorizontalLayout(self.__group_box,
                                                     QtCore.QRect(350, 200, 400, 50),
                                                     "ResultLayout")

        Label = Ui_Label(packet_rate_horizontal.widget)
        OutputBox = Ui_OutputBox(packet_rate_horizontal.widget)

        packet_rate_horizontal.layout.setAlignment(QtCore.Qt.AlignLeft)
        packet_rate_horizontal.layout.addStretch(1)

        self.label_7 = Label.setup("label_7", QtCore.QSize(120, 31))
        packet_rate_horizontal.layout.addWidget(self.label_7)
        packet_rate_horizontal.layout.addSpacing(5)

        self.output_for_packet_rate = OutputBox.setup("OutForPPS", QtCore.QSize(100, 31))
        packet_rate_horizontal.layout.addWidget(self.output_for_packet_rate)

        self.label_8 = Label.setup("label_8", QtCore.QSize(60, 31))
        packet_rate_horizontal.layout.addWidget(self.label_8)

    def __retranslate_Ui(self):
        translate = QtCore.QCoreApplication.translate
        self.__group_box.setTitle(translate("MainWindow", "Result"))
        self.label_5.setText(translate("MainWindow", "Bandwidth:"))
        self.label_6.setText(translate("MainWindow", "kbps"))
        self.label_7.setText(translate("MainWindow", "Packet rate:"))
        self.label_8.setText(translate("MainWindow", "pps"))
