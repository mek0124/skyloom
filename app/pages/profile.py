from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QPushButton,
    QListWidget, QListWidgetItem
)

from PySide6.QtCore import Qt

from ..models.user import User
from .components.profile_left import ProfileLeftSide


class Profile(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Profile")

        self.color_theme = parent.color_theme
        self.db = parent.db
        self.user = self.load_user(parent.user)

        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignCenter)

        layout.addWidget(ProfileLeftSide(self), 1)

        self.add_right_box(layout)

        layout.addStretch()

    def load_user(self, user):
        if user:
            self.username = user.username
            self.created_at = user.created_at

            if user.updated_at != user.created_at:
                self.updated_at = user.updated_at


            self.addresses = user.addresses
            self.settings = user.settings
    
    def add_addresses(self, layout):
        addresses_row = QWidget()
        addresses_row.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}
            """
        )

        addresses_row_layout = QVBoxLayout(addresses_row)
        addresses_row_layout.setContentsMargins(0, 0, 0, 0)
        addresses_row_layout.setSpacing(5)
        addresses_row_layout.setAlignment(Qt.AlignLeft)

        addresses_label = QLabel("Current Addresses")
        addresses_label.setStyleSheet(
            f"""
                QLabel {{
                    font-weight: bold;
                    font-style: italic;
                    font-size: 14px;
                    letter-spacing: 0.2em;
                    color: {self.color_theme['primary']};
                }}
            """
        )

        self.addresses_box = QListWidget()
        self.addresses_box.setStyleSheet(
            f"""
                QListWidget {{
                    border: none;
                    background-color: transparent;
                }}
                
                QListWidget::item {{
                    color: {self.color_theme['text_primary']};
                    font-size: 8px;
                }}

                QListWidget::item:hover {{
                    background-color: {self.color_theme['surface_glass_hover']};
                }}

                QListWidget::item:selected {{
                    background-color: {self.color_theme['surface_glass']};
                }}
            """
        )

        address_edit_row = QWidget()
        address_edit_row.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}
            """
        )

        address_edit_row_layout = QHBoxLayout(address_edit_row)
        address_edit_row_layout.setContentsMargins(0, 0, 0, 0)
        address_edit_row_layout.setSpacing(10)
        address_edit_row_layout.setAlignment(Qt.AlignCenter)

        address_edit_label = QLabel("Add/Edit Address")
        address_edit_label.setStyleSheet(
            f"""
                QLabel {{
                    font-style: italic;
                    font-size: 12px;
                    color: {self.color_theme['text_primary']};
                }}
            """
        )

        self.address_edit = QLineEdit()
        self.address_edit.setAlignment(Qt.AlignCenter)
        self.address_edit.setFixedWidth(250)
        self.address_edit.setStyleSheet(
            f"""
                QLineEdit {{
                    font-size: 12px;
                    border-bottom: 2px solid {self.color_theme['primary']};
                    color: {self.color_theme['text_primary']}
                }}
            """
        )

        update_address_btn = QPushButton("Add/Edit")
        update_address_btn.setFixedSize(50, 20)
        update_address_btn.setStyleSheet(
            f"""
                QPushButton {{
                    background-color: transparent;
                    border: 1px solid {self.color_theme['primary']};
                    border-radius: {self.color_theme['border_radius_small']};
                    color: {self.color_theme['text_primary']};
                    font-size: 10px;
                }}

                QPushButton:hover {{
                    background-color: {self.color_theme['surface_glass_hover']};
                }}
            """
        )

        address_edit_row_layout.addWidget(address_edit_label)
        address_edit_row_layout.addWidget(self.address_edit)
        address_edit_row_layout.addWidget(update_address_btn)

        addresses_row_layout.addWidget(addresses_label)
        addresses_row_layout.addWidget(self.addresses_box)
        addresses_row_layout.addWidget(address_edit_row)

        layout.addWidget(addresses_row, 2)
        return layout
    
    def add_right_box(self, layout):
        user_settings = QWidget()
        user_settings.setStyleSheet(
            f"""
                QWidget {{
                    background-color: transparent;
                }}
            """
        )

        user_settings_layout = QVBoxLayout(user_settings)
        user_settings_layout.setContentsMargins(10, 10, 10, 10)
        user_settings_layout.setSpacing(10)
        user_settings_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        title = QLabel("Settings")
        title.setStyleSheet(
            f"""
                QLabel {{
                    font-weight: bold;
                    font-style: italic;
                    font-size: 14px;
                    letter-spacing: 0.2em;
                    color: {self.color_theme['primary']};
                }}
            """
        )

        user_settings_layout.addWidget(title)
        user_settings_layout.addStretch()

        layout.addWidget(user_settings, 1)
        return layout