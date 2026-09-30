# Horizontal Box Layout

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtCore import QCoreApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First App")

        # Layout
        hbox = QHBoxLayout()
        self.setLayout(hbox)

        # button widget
        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)
        btn3 = QPushButton("Button 3", self)

        # adding widget to layout
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)


app = QCoreApplication.instance()
if app is None:
    app = QApplication([])

window = MainWindow()
window.show()
app.exec()
