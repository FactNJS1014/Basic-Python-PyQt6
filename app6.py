# Horizontal Box Layout

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt6.QtCore import QCoreApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First App")

        # Layout
        grid = QGridLayout()
        self.setLayout(grid)

        # button widget
        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)
        btn3 = QPushButton("Button 3", self)
        btn4 = QPushButton("Button 4", self)
        btn5 = QPushButton("Button 5", self)
        btn6 = QPushButton("Button 6", self)

        # adding widget to layout
        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 1, 0)
        grid.addWidget(btn5, 1, 1)
        grid.addWidget(btn6, 1, 2)


app = QCoreApplication.instance()
if app is None:
    app = QApplication([])

window = MainWindow()
window.show()
app.exec()
