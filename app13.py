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

        btn1 = QPushButton("Info")
        btn2 = QPushButton("Warning")
        btn3 = QPushButton("Error")

        btn1.clicked.connect(self.showMessage)
        btn2.clicked.connect(self.showMessage)
        btn3.clicked.connect(self.showMessage)

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

    def showMessage(self):  # slot
        sender = self.sender()
        if sender.text() == "Info":
            QMessageBox.information(self, "Button Info", "Button is clicked")
        elif sender.text() == "Warning":
            QMessageBox.warning(self, "Button Warning", "Button is clicked")
        elif sender.text() == "Error":
            QMessageBox.critical(self, "Button Error", "Button is clicked")


app = QCoreApplication.instance()
if app is None:
    app = QApplication([])


window = MainWindow()
window.show()
app.exec()
