# จัดการ Widget ด้วย Method

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtCore import QCoreApplication, QSize


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First App")
        self.setFixedSize(QSize(400, 300))

        # Layout
        layout = QHBoxLayout()
        self.setLayout(layout)

        # self.display_button("Open", layout)
        # self.display_button("Save", layout)
        # self.display_button("Exit", layout)
        message = ["Open", "Save", "Exit"]
        for i in message:
            self.display_button(i, layout)

    def display_button(self, text, layout):
        btn = QPushButton(text)
        btn.setFixedSize(QSize(100, 50))
        layout.addWidget(btn)


app = QCoreApplication.instance()
if app is None:
    app = QApplication([])

window = MainWindow()
window.show()
app.exec()
