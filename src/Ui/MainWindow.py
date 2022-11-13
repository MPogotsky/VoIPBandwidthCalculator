from PyQt5 import QtCore, QtWidgets
from src.Ui.Components.Parameters import Parameters
from src.Ui.Components.Results import Results


class Ui_MainWindow(object):
    def __init__(self):
        self.parameters = None
        self.upper_menu = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        central_widget = QtWidgets.QWidget(MainWindow)

        MainWindow.setCentralWidget(central_widget)

        Parameters(MainWindow, central_widget)
        Results(MainWindow, central_widget)

        translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(translate("MainWindow", "MainWindow"))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
