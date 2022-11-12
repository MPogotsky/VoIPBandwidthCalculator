from PyQt5 import QtWidgets, QtCore

from src.Ui.Widgets.RadioButton import Ui_RadioButton
from src.Ui.Widgets.ComboBox import Ui_ComboBox
from src.Ui.Widgets.Label import Ui_Label
from src.Ui.Widgets.InputBox import Ui_InputBox
from src.Ui.Widgets.GroupBox import Ui_GroupBox
from src.Ui.Layouts.Vertical import Ui_VerticalLayout
from src.Ui.Layouts.Grid import Ui_GridLayout
from src.Ui.Layouts.Horizontal import Ui_HorizontalLayout


class Parameters(object):
    def __init__(self, Window):
        self.__Window = Window
        self.GroupBox = Ui_GroupBox()
        self.CentralWidget = QtWidgets.QWidget(self.__Window)
        self.CentralWidget.setObjectName("centralwidget")
        self.__initDependencies()

    def setupUi(self):
        self.__setupDependencies()
        self.__raiseObjects()

    def __initDependencies(self):
        self.main_layout = Ui_VerticalLayout(self.CentralWidget,
                                             QtCore.QRect(9, 9, 1190, 750),
                                             "MainLayout")
        self.group_box_parameters = self.GroupBox.setup("Parameters",
                                                        QtCore.QSize(1160, 410),
                                                        self.main_layout.widget)
        self.button_group = QtWidgets.QButtonGroup()

    def __setupDependencies(self):
        self.__Window.setCentralWidget(self.CentralWidget)

        self.__setupPayload()
        self.__setupRTP()
        self.__setupUDP()
        self.__setupIP()
        self.__setupLink()
        self.__setupInputForChannels()

    def __setupPayload(self):
        payload_grid = Ui_GridLayout(self.group_box_parameters,
                                     QtCore.QRect(40, 30, 1000, 100),
                                     "payloadLayout")
        RadioButton = Ui_RadioButton(payload_grid.widget)
        self.radio_button_payload = RadioButton.setup("Payload", QtCore.QSize(131, 31))
        payload_grid.layout.addWidget(self.radio_button_payload, 0, 0, 1, 1)

        self.button_group.addButton(self.radio_button_payload)

        ComboBox = Ui_ComboBox(payload_grid.widget)
        self.combo_box_payload = ComboBox.setup("PayloadComboBox", QtCore.QSize(180, 31))
        payload_grid.layout.addWidget(self.combo_box_payload, 0, 1, 1, 1)

        InputBox = Ui_InputBox(payload_grid.widget)
        self.input_box_for_ms = InputBox.setup("InputForMS", QtCore.QSize(111, 31))
        payload_grid.layout.addWidget(self.input_box_for_ms, 0, 4, 1, 1)
        self.input_box_for_frames = InputBox.setup("InputForFrames", QtCore.QSize(111, 31))
        payload_grid.layout.addWidget(self.input_box_for_frames, 1, 4, 1, 1)

        Label = Ui_Label(payload_grid.widget)
        self.label_1 = Label.setup("label", QtCore.QSize(51, 21))
        payload_grid.layout.addWidget(self.label_1, 0, 2, 1, 1)
        self.label_2 = Label.setup("label_2", QtCore.QSize(41, 31))
        payload_grid.layout.addWidget(self.label_2, 0, 5, 1, 1)
        self.label_3 = Label.setup("label_3", QtCore.QSize(221, 31))
        payload_grid.layout.addWidget(self.label_3, 1, 5, 1, 1)

    def __setupRTP(self):
        RTP_horizontal = Ui_HorizontalLayout(self.group_box_parameters,
                                             QtCore.QRect(40, 130, 650, 50),
                                             "RTPLayout")
        RadioButton = Ui_RadioButton(RTP_horizontal.widget)

        self.radio_button_RTP = RadioButton.setup("RTP", QtCore.QSize(131, 31))
        RTP_horizontal.layout.addWidget(self.radio_button_RTP)

        self.button_group.addButton(self.radio_button_RTP)

    def __setupUDP(self):
        UDP_horizontal = Ui_HorizontalLayout(self.group_box_parameters,
                                             QtCore.QRect(40, 180, 650, 50),
                                             "UDPLayout")

        RadioButton = Ui_RadioButton(UDP_horizontal.widget)
        self.radio_button_UDP = RadioButton.setup("UDP", QtCore.QSize(131, 31))
        UDP_horizontal.layout.addWidget(self.radio_button_UDP)

        self.button_group.addButton(self.radio_button_UDP)

    def __setupIP(self):
        IP_horizontal = Ui_HorizontalLayout(self.group_box_parameters,
                                            QtCore.QRect(40, 230, 650, 50),
                                            "IPLayout")

        RadioButton = Ui_RadioButton(IP_horizontal.widget)
        ComboBox = Ui_ComboBox(IP_horizontal.widget)

        self.radio_button_IP = RadioButton.setup("IP", QtCore.QSize(131, 31))
        IP_horizontal.layout.addWidget(self.radio_button_IP)

        self.button_group.addButton(self.radio_button_IP)

        self.combo_box_IP_version = ComboBox.setup("IPVersionComboBox", QtCore.QSize(180, 31))
        sp = self.combo_box_IP_version.sizePolicy()
        sp.setHorizontalPolicy(QtWidgets.QSizePolicy.Fixed)
        self.combo_box_IP_version.setSizePolicy(sp)
        IP_horizontal.layout.setAlignment(QtCore.Qt.AlignLeft)
        IP_horizontal.layout.addWidget(self.combo_box_IP_version)

    def __setupLink(self):
        link_horizontal = Ui_HorizontalLayout(self.group_box_parameters,
                                              QtCore.QRect(40, 280, 700, 50),
                                              "LinkLayout")
        RadioButton = Ui_RadioButton(link_horizontal.widget)

        self.radio_button_link = RadioButton.setup("Link", QtCore.QSize(160, 31))
        link_horizontal.layout.addWidget(self.radio_button_link)

        self.button_group.addButton(self.radio_button_link)

    def __setupInputForChannels(self):
        channels_horizontal = Ui_HorizontalLayout(self.group_box_parameters,
                                                  QtCore.QRect(300, 350, 650, 50),
                                                  "InputForChannelsLayout")
        InputBox = Ui_InputBox(channels_horizontal.widget)
        Label = Ui_Label(channels_horizontal.widget)

        self.label_4 = Label.setup("label_4", QtCore.QSize(250, 31))
        channels_horizontal.layout.addWidget(self.label_4)
        channels_horizontal.layout.addSpacing(5)
        self.input_box_for_channels = InputBox.setup("InputForChannels", QtCore.QSize(100, 31))
        sp = self.input_box_for_channels.sizePolicy()
        sp.setHorizontalPolicy(QtWidgets.QSizePolicy.Fixed)
        self.input_box_for_channels.setSizePolicy(sp)
        channels_horizontal.layout.setAlignment(QtCore.Qt.AlignLeft)
        channels_horizontal.layout.addWidget(self.input_box_for_channels)

    def __raiseObjects(self):
        self.radio_button_payload.raise_()
        self.combo_box_payload.raise_()

        self.label_1.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.input_box_for_ms.raise_()
        self.input_box_for_frames.raise_()

        self.radio_button_RTP.raise_()
        self.radio_button_UDP.raise_()
        self.radio_button_IP.raise_()
        self.combo_box_IP_version.raise_()
        self.radio_button_link.raise_()

        self.input_box_for_channels.raise_()

    def retranslateUi(self, translate: QtCore.QCoreApplication.translate):
        self.group_box_parameters.setTitle(translate("MainWindow", "Parameters"))
        self.radio_button_payload.setText(translate("MainWindow", "Payload is"))
        self.label_1.setText(translate("MainWindow", "with"))
        self.label_2.setText(translate("MainWindow", "ms"))
        self.label_3.setText(translate("MainWindow", "frames per packet"))
        self.radio_button_RTP.setText(translate("MainWindow", "RTP protocol header"))
        self.radio_button_UDP.setText(translate("MainWindow", "UDP protocol header"))
        self.radio_button_IP.setText(translate("MainWindow", "IP protocol version"))
        self.radio_button_link.setText(translate("MainWindow", "Link layer header(Includes Layer 1 and Layer 2)"))
        self.label_4.setText(translate("MainWindow", "For a number of channels"))