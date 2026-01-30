from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel
)

from PySide6.QtCore import Qt

from .components.profile_left import ProfileLeftSide
from .components.profile_right import ProfileRightSide


class Profile(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Profile")

        self.color_theme = parent.color_theme
        self.user = parent.user

        self.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}

                QWidget#user-settings {{
                    background-color: transparent;
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
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignCenter)

        layout.addWidget(ProfileLeftSide(self), 1)
        layout.addWidget(ProfileRightSide(self), 1)

        layout.addStretch()

    def load_user(self, user):
        if user:
            self.settings = user.settings
    
    def add_right_box(self, layout):
        user_settings = QWidget()
        user_settings.setObjectName("user-settings")

        user_settings_layout = QVBoxLayout(user_settings)
        user_settings_layout.setContentsMargins(10, 10, 10, 10)
        user_settings_layout.setSpacing(10)
        user_settings_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        title = QLabel("Settings")
        title.setObjectName("title")

        user_settings_layout.addWidget(title)
        user_settings_layout.addStretch()

        layout.addWidget(user_settings, 1)
        return layout