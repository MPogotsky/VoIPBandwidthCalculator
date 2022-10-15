from PyQt5 import QtCore, QtWidgets, QtGui

from ..UiUtils.GroupBox import Ui_GroupBox
from ..UiUtils.RadioButton import Ui_RadioButton
from ..UiUtils.ComboBox import Ui_ComboBox

class Ui_MainWindow(object):
    def __init__(self):
        self.groupBox = Ui_GroupBox()
        self.radioButton = Ui_RadioButton()
        self.comboBox = Ui_ComboBox()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1134, 755)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralwidget")

        self.ui_grb_parameters = self.groupBox.setup("Parameters", QtCore.QRect(10, 10, 1111, 331), self.centralWidget)
        self.ui_rbtn_payload = self.radioButton.setup("Payload", QtCore.QRect(200, 20, 131, 31), self.ui_grb_parameters)
        self.ui_cmbbx_standardComboBox = self.comboBox.setup("StandardComboBox", QtCore.QRect(340, 21, 151, 31), self.ui_grb_parameters)

        self.label = QtWidgets.QLabel(self.ui_grb_parameters)
        self.label.setGeometry(QtCore.QRect(510, 25, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.inputForMS = QtWidgets.QPlainTextEdit(self.ui_grb_parameters)
        self.inputForMS.setGeometry(QtCore.QRect(570, 20, 111, 31))
        self.inputForMS.setObjectName("inputForMS")
        self.label_2 = QtWidgets.QLabel(self.ui_grb_parameters)
        self.label_2.setGeometry(QtCore.QRect(690, 20, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.ui_grb_parameters)
        self.label_3.setGeometry(QtCore.QRect(690, 60, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.inputForFrames = QtWidgets.QPlainTextEdit(self.ui_grb_parameters)
        self.inputForFrames.setGeometry(QtCore.QRect(570, 60, 111, 31))
        self.inputForFrames.setObjectName("inputForFrames")
        self.RTP = QtWidgets.QRadioButton(self.ui_grb_parameters)
        self.RTP.setGeometry(QtCore.QRect(200, 110, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.RTP.setFont(font)
        self.RTP.setChecked(False)
        self.RTP.setObjectName("RTP")
        self.UDP = QtWidgets.QRadioButton(self.ui_grb_parameters)
        self.UDP.setGeometry(QtCore.QRect(200, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.UDP.setFont(font)
        self.UDP.setChecked(False)
        self.UDP.setObjectName("UDP")
        self.IP = QtWidgets.QRadioButton(self.ui_grb_parameters)
        self.IP.setGeometry(QtCore.QRect(200, 190, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.IP.setFont(font)
        self.IP.setChecked(False)
        self.IP.setObjectName("IP")
        self.Payload_5 = QtWidgets.QRadioButton(self.ui_grb_parameters)
        self.Payload_5.setGeometry(QtCore.QRect(200, 230, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Payload_5.setFont(font)
        self.Payload_5.setChecked(False)
        self.Payload_5.setObjectName("Payload_5")
        self.LinkHeadersComboBox = QtWidgets.QComboBox(self.ui_grb_parameters)
        self.LinkHeadersComboBox.setGeometry(QtCore.QRect(360, 230, 151, 31))
        self.LinkHeadersComboBox.setObjectName("LinkHeadersComboBox")
        self.RTPTypesComboBox = QtWidgets.QComboBox(self.ui_grb_parameters)
        self.RTPTypesComboBox.setGeometry(QtCore.QRect(300, 110, 151, 31))
        self.RTPTypesComboBox.setObjectName("RTPTypesComboBox")
        self.label_4 = QtWidgets.QLabel(self.ui_grb_parameters)
        self.label_4.setGeometry(QtCore.QRect(360, 280, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.inputForMS_2 = QtWidgets.QPlainTextEdit(self.ui_grb_parameters)
        self.inputForMS_2.setGeometry(QtCore.QRect(650, 280, 111, 31))
        self.inputForMS_2.setObjectName("inputForMS_2")
        self.ui_rbtn_payload.raise_()
        self.ui_cmbbx_standardComboBox.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.inputForMS.raise_()
        self.inputForFrames.raise_()
        self.label.raise_()
        self.RTP.raise_()
        self.UDP.raise_()
        self.IP.raise_()
        self.Payload_5.raise_()
        self.LinkHeadersComboBox.raise_()
        self.RTPTypesComboBox.raise_()
        self.label_4.raise_()
        self.inputForMS_2.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1134, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ui_grb_parameters.setTitle(_translate("MainWindow", "Parameters"))
        self.ui_rbtn_payload.setText(_translate("MainWindow", "Payload is"))
        self.label.setText(_translate("MainWindow", "with"))
        self.label_2.setText(_translate("MainWindow", "ms"))
        self.label_3.setText(_translate("MainWindow", "frames per packet"))
        self.RTP.setText(_translate("MainWindow", "RTP is"))
        self.UDP.setText(_translate("MainWindow", "UDP"))
        self.IP.setText(_translate("MainWindow", "IP"))
        self.Payload_5.setText(_translate("MainWindow", "Link header"))
        self.label_4.setText(_translate("MainWindow", "For a number of channels"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))