import sys
import os
from PyQt5 import QtWidgets, QtGui
from src.Ui.MainWindow import Ui_MainWindow

basedir = os.path.dirname(__file__)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    basedir = os.path.dirname(__file__)
    print(os.path.join(basedir, "dependency", 'pwr.ico'))
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, "dependency", 'pwr.png')))
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(1180, 800)
    MainWindow.setWindowIcon(QtGui.QIcon(os.path.join(basedir, "dependency", 'pwr.ico')))
    ui = Ui_MainWindow()
    ui.setup_Ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
