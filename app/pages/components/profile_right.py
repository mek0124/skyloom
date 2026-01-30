from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt

from .profile.settings_tree import SettingsTree


class ProfileRightSide(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.color_theme = parent.color_theme
        self.user = parent.user
        self.setStyleSheet(
            f"""
                QWidget {{ 
                    border: none; 
                    background-color: transparent;
                }}
            """
        )

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        layout.addWidget(SettingsTree(self))