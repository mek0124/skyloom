from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, 
    QRadioButton
)

from PySide6.QtCore import Qt


class Support(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Support")

        self.color_theme = parent.color_theme

        self.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}

                QLabel#title {{
                    font-weight: bold;
                    font-style: italic;
                    font-size: 14px;
                    letter-spacing: 0.2em;
                    color: {self.color_theme['primary']};
                }}
            """
        )

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Skyloom Support")
        title.setObjectName("title")

        layout.addWidget(title)

        layout.addStretch()