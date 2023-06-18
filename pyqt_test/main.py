from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    

def clicked():
    print('Cliked!')

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,600,400)
    win.setWindowTitle('UniSystem')

    for i in range(10):
        b1 = QtWidgets.QPushButton(win)
        b1.setText('Ok')
        b1.move(i*100,10)
        b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec())

window()