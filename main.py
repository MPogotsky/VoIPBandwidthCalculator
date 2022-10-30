import sys
from PyQt5 import QtWidgets
from src.Windows.MainWindow import Ui_MainWindow
from src.VoIP_Calculator.VoIP_Calculator import calculate

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    calculate()
