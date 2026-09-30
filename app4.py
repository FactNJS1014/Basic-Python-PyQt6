# Vertical Box Layout

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import QCoreApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First App")

        # Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # button widget
        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)
        btn3 = QPushButton("Button 3", self)

        # adding widget to layout
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)


app = QCoreApplication.instance()
if app is None:
    app = QApplication([])

window = MainWindow()
window.show()
app.exec()
