from PyQt5 import QtCore, QtWidgets

from src.Ui.Components.ComponentManager import ComponentManager

from src.VoIP_Calculator.CalculatorVoIP import CalculatorVoIP


class Ui_MainWindow(object):
    def __init__(self):
        self.parameters = None
        self.upper_menu = None

    def setup_Ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        central_widget = QtWidgets.QWidget(MainWindow)

        MainWindow.setCentralWidget(central_widget)

        calculator = CalculatorVoIP()

        ComponentManager(MainWindow, central_widget, calculator)

        translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(translate("MainWindow", "VoIP Bandwidth Calculator"))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
