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
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.setLayout(layout)

        # widgets
        lb = QLabel("Hello World")
        btn1 = QPushButton("Submit")
        btn2 = QPushButton("Cancel")

        layout.addWidget(lb)
        layout.addWidget(btn1)
        layout.addWidget(btn2)


app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

window = MainWindow()
window.show()
app.exec()
