from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QRadioButton, QPushButton
)

from PySide6.QtCore import Qt


class SettingsTree(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.color_theme = parent.color_theme
        self.user = parent.user

        self.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}
            """
        )

        self.setup_ui()
        self.load_user_settings()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentMargsin(10, 10, 10, 10)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

    def load_user_settings(self):
        if not self.user['settings']:
            pass