# QSS StyleSheet

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtCore import QCoreApplication, QSize, Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First App")
        self.setFixedSize(QSize(800, 600))

        # Layout
        layout = QHBoxLayout()
        layout.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        layout.setSpacing(20)
        self.setLayout(layout)

        message = ["Open", "Save", "Exit"]
        for i in message:
            self.display_button(i, layout)

    def display_button(self, text, layout):
        btn = QPushButton(text)
        btn.setFixedSize(QSize(100, 50))
        btn.setStyleSheet(
            """
            color: white;
            background-color: #06d6a0;
            font-size: 18px;
            """
        )
        layout.addWidget(btn)


app = QCoreApplication.instance()
if app is None:
    app = QApplication([])

window = MainWindow()
window.show()
app.exec()
