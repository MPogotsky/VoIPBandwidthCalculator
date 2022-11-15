import sys
import os
from PyQt5 import QtWidgets, QtGui
from src.Ui.MainWindow import Ui_MainWindow

if __name__ == "__main__":
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(1180, 800)
    MainWindow.setWindowIcon(QtGui.QIcon("dependency/pwr.ico"))
    ui = Ui_MainWindow()
    ui.setup_Ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
