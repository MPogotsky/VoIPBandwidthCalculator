from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QHBoxLayout

from src.Ui.Widgets.RadioButton import Ui_RadioButton
from src.Ui.Widgets.ComboBox import Ui_ComboBox
from src.Ui.Widgets.Label import Ui_Label
from src.Ui.Widgets.InputBox import Ui_InputBox
from src.Ui.Widgets.GroupBox import Ui_GroupBox
from src.Ui.Layouts.Vertical import Ui_VerticalLayout
from src.Ui.Layouts.Grid import Ui_GridLayout
from src.Ui.Layouts.Horizontal import Ui_HorizontalLayout


class Ui_GroupBoxManager(object):
    def __init__(self, Window):
        self.__Window = Window
        self.groupBox = Ui_GroupBox()
        self.centralWidget = QtWidgets.QWidget(self.__Window)
        self.centralWidget.setObjectName("centralwidget")
        self.__initDependencies()

    def setupUi(self):
        self.__setupDependencies()
        self.__raiseObjects()

    def __initDependencies(self):
        self.mainLayout = Ui_VerticalLayout(self.centralWidget, QtCore.QRect(9, 9, 1190, 750), "mainLayout")

        self.groupBox_parameters = self.groupBox.setup("Parameters", QtCore.QSize(1160, 410),
                                                       self.mainLayout.widget)

        self.payload_grid = Ui_GridLayout(self.groupBox_parameters, QtCore.QRect(29, 29, 1000, 298), "payloadLayout")

        # self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_parameters)
        # self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 350, 650, 41))
        # self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        # self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        # self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout.setObjectName("horizontalLayout")

        self.horizontal_layout = Ui_HorizontalLayout(self.groupBox_parameters, QtCore.QRect(300, 350, 650, 41), "horizontalLayout")


        self.radioButton = Ui_RadioButton(self.payload_grid.widget)
        self.comboBox = Ui_ComboBox(self.payload_grid.widget)
        self.label_on_grid = Ui_Label(self.payload_grid.widget)
        self.label_on_horizontal = Ui_Label(self.horizontal_layout.widget)
        self.inputBox = Ui_InputBox(self.payload_grid.widget)

    def __setupDependencies(self):
        self.__Window.setCentralWidget(self.centralWidget)

        self.radioButton_payload = self.radioButton.setup("Payload", QtCore.QSize(131, 31))
        self.payload_grid.layout.addWidget(self.radioButton_payload, 0, 0, 1, 1)
        self.comboBox_payload = self.comboBox.setup("PayloadComboBox", QtCore.QSize(180, 31))
        self.payload_grid.layout.addWidget(self.comboBox_payload, 0, 1, 1, 1)

        self.label_1 = self.label_on_grid.setup("label", QtCore.QSize(51, 21))
        self.payload_grid.layout.addWidget(self.label_1, 0, 2, 1, 1)
        self.label_2 = self.label_on_grid.setup("label_2", QtCore.QSize(41, 31))
        self.payload_grid.layout.addWidget(self.label_2, 0, 5, 1, 1)
        self.label_3 = self.label_on_grid.setup("label_3", QtCore.QSize(221, 31))
        self.payload_grid.layout.addWidget(self.label_3, 1, 5, 1, 1)

        self.__setupInputForMs()

        self.radioButton_RTP = self.radioButton.setup("RTP", QtCore.QSize(131, 31))
        self.payload_grid.layout.addWidget(self.radioButton_RTP, 2, 0, 1, 1)
        # self.comboBox_RTP_types = self.comboBox.setup("RTPTypesComboBox", QtCore.QSize(180, 31))
        # self.gridLayout.addWidget(self.comboBox_RTP_types, 2, 1, 1, 1)

        self.radioButton_UDP = self.radioButton.setup("UDP", QtCore.QSize(131, 31))
        self.payload_grid.layout.addWidget(self.radioButton_UDP, 3, 0, 1, 1)

        self.__setupIP()

        self.radioButton_link = self.radioButton.setup("Link", QtCore.QSize(160, 31))
        self.payload_grid.layout.addWidget(self.radioButton_link, 5, 0, 1, 1)
        self.comboBox_link_headers = self.comboBox.setup("LinkHeadersComboBox", QtCore.QSize(180, 31))
        self.payload_grid.layout.addWidget(self.comboBox_link_headers, 5, 1, 1, 1)

        self.__setupInputForChannels()

    def __setupInputForMs(self):
        self.inputBox_for_ms = self.inputBox.setup("InputForMS", QtCore.QSize(111, 31))
        self.payload_grid.layout.addWidget(self.inputBox_for_ms, 0, 4, 1, 1)
        self.inputBox_for_frames = self.inputBox.setup("InputForFrames", QtCore.QSize(111, 31))
        self.payload_grid.layout.addWidget(self.inputBox_for_frames, 1, 4, 1, 1)

    def __setupIP(self):
        horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_parameters)
        horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 250, 650, 41))
        horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        horizontalLayout = QtWidgets.QHBoxLayout(horizontalLayoutWidget)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setObjectName("horizontalLayout")

        self.radioButton_IP = self.radioButton.setup("IP", QtCore.QSize(131, 31))
        horizontalLayout.addWidget(self.radioButton_IP)
        horizontalLayout.addSpacing(5)

        self.comboBox_IP_version = self.comboBox.setup("IPVersionComboBox", QtCore.QSize(180, 31))
        sp = self.comboBox_IP_version.sizePolicy()
        sp.setHorizontalPolicy(QtWidgets.QSizePolicy.Fixed)
        self.comboBox_IP_version.setSizePolicy(sp)
        horizontalLayout.setAlignment(QtCore.Qt.AlignLeft)
        horizontalLayout.addWidget(self.comboBox_IP_version)

    def __setupInputForChannels(self):
        self.label_4 = self.label_on_horizontal.setup("label_4", QtCore.QSize(250, 31))
        self.horizontal_layout.layout.addWidget(self.label_4)
        self.horizontal_layout.layout.addSpacing(5)
        self.inputBox_for_channels = self.inputBox.setup("InputForChannels", QtCore.QSize(100, 31))
        sp = self.inputBox_for_channels.sizePolicy()
        sp.setHorizontalPolicy(QtWidgets.QSizePolicy.Fixed)
        self.inputBox_for_channels.setSizePolicy(sp)
        self.horizontal_layout.layout.setAlignment(QtCore.Qt.AlignLeft)
        self.horizontal_layout.layout.addWidget(self.inputBox_for_channels)

    def __raiseObjects(self):
        self.radioButton_payload.raise_()
        self.comboBox_payload.raise_()

        self.label_1.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.inputBox_for_ms.raise_()
        self.inputBox_for_frames.raise_()

        self.radioButton_RTP.raise_()
        # self.comboBox_RTP_types.raise_()

        self.radioButton_UDP.raise_()
        self.radioButton_IP.raise_()

        self.radioButton_link.raise_()
        self.comboBox_link_headers.raise_()

        self.inputBox_for_channels.raise_()

    def retranslateUi(self, translate: QtCore.QCoreApplication.translate):
        self.groupBox_parameters.setTitle(translate("MainWindow", "Parameters"))
        self.radioButton_payload.setText(translate("MainWindow", "Payload is"))
        self.label_1.setText(translate("MainWindow", "with"))
        self.label_2.setText(translate("MainWindow", "ms"))
        self.label_3.setText(translate("MainWindow", "frames per packet"))
        self.radioButton_RTP.setText(translate("MainWindow", "RTP is"))
        self.radioButton_UDP.setText(translate("MainWindow", "UDP"))
        self.radioButton_IP.setText(translate("MainWindow", "IP"))
        self.radioButton_link.setText(translate("MainWindow", "Link header"))
        self.label_4.setText(translate("MainWindow", "For a number of channels"))
