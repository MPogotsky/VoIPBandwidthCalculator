from PyQt5 import QtCore, QtWidgets

from src.Ui.Components.ComponentManager import ComponentManager
from src.Ui.Components.Parameters import Parameters
from src.Ui.Components.Results import Results

from src.VoIP_Calculator.VoIP_Calculator import VoIP_Calculator


class Ui_MainWindow(object):
    def __init__(self):
        self.parameters = None
        self.upper_menu = None

    def setup_Ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        central_widget = QtWidgets.QWidget(MainWindow)

        MainWindow.setCentralWidget(central_widget)

        calculator = VoIP_Calculator()

        ComponentManager(MainWindow, central_widget, calculator)

        translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(translate("MainWindow", "MainWindow"))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
