from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton,
    QListWidget, QListWidgetItem
)

from PySide6.QtCore import Qt

from .user_details import UserDetails
from .user_addresses import UserAddresses


class ProfileLeftSide(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.color_theme = parent.color_theme
        self.user = parent.user
        self.setStyleSheet("QWidget {{ border: none; }}")

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignTop)

        layout.addWidget(UserDetails(self))
        layout.addWidget(UserAddresses(self))