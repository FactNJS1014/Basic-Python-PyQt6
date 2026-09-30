import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("เครื่องคิดเลข")

        grid = QGridLayout(self)

        # จอแสดงผล: แถว 0, คอลัมน์ 0, สูง 1 แถว, กว้าง 4 คอลัมน์
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        grid.addWidget(self.display, 0, 0, 1, 4)

        # (ข้อความ, แถว, คอลัมน์, จำนวนแถว, จำนวนคอลัมน์)
        buttons = [
            ("C", 1, 0, 1, 3),
            ("/", 1, 3, 1, 1),
            ("7", 2, 0, 1, 1),
            ("8", 2, 1, 1, 1),
            ("9", 2, 2, 1, 1),
            ("*", 2, 3, 1, 1),
            ("4", 3, 0, 1, 1),
            ("5", 3, 1, 1, 1),
            ("6", 3, 2, 1, 1),
            ("-", 3, 3, 1, 1),
            ("1", 4, 0, 1, 1),
            ("2", 4, 1, 1, 1),
            ("3", 4, 2, 1, 1),
            ("+", 4, 3, 1, 1),
            ("0", 5, 0, 1, 2),
            ("=", 5, 2, 1, 2),
        ]
        for text, row, col, row_span, col_span in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(lambda _checked, t=text: self.on_button(t))
            grid.addWidget(btn, row, col, row_span, col_span)

    def on_button(self, text):
        if text == "C":
            self.display.clear()
        elif text == "=":
            try:
                # รับเฉพาะตัวเลขและเครื่องหมายจากปุ่มเท่านั้น จึงใช้ eval ได้ในตัวอย่างนี้
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception:
                self.display.setText("ผิดพลาด")
        else:
            self.display.setText(self.display.text() + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
