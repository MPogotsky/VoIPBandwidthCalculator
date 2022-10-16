from PyQt5 import QtCore, QtWidgets
from ..UiTemplates.GroupBox import Ui_GroupBox
from ..UiManager.GroupBoxManager import Ui_GroupBoxManager

class Ui_MainWindow(object):
    def __init__(self):
        self.groupBox = Ui_GroupBox()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1134, 755)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralwidget")

        self.groupBox_parameters = self.groupBox.setup("Parameters", QtCore.QRect(10, 10, 1111, 331),
                                                          self.centralWidget)
        self.ui_parameters = Ui_GroupBoxManager(self.groupBox_parameters)
        self.ui_parameters.setupUi()

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

        self.ui_parameters.raiseObjects()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.groupBox_parameters.setTitle(_translate("MainWindow", "Parameters"))
        self.ui_parameters.retranslateUi(_translate)

        self.menuFile.setTitle(_translate("MainWindow", "File"))
