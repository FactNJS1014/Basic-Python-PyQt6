# QSS StyleSheet

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First App")
        self.setFixedSize(QSize(400, 300))

        # Layout
        layout = QVBoxLayout()

        self.setLayout(layout)

        # widgets

        btn1 = QPushButton("Button01")
        btn1.clicked.connect(self.showName)  # signal
        layout.addWidget(btn1)

    def showName(self):  # slot
        print(self.sender().text())
        # QMessageBox.information(self, "Button Info", "Button is clicked")


app = QCoreApplication.instance()
if app is None:
    app = QApplication([])


window = MainWindow()
window.show()
app.exec()
