from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QPushButton,
    QListWidget, QListWidgetItem
)

from PySide6.QtCore import Qt

from ..models.user import User


class Profile(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Profile")

        self.color_theme = parent.color_theme
        self.db = parent.db
        self.user = self.load_user(parent.user)

        self.username = None
        self.created_at = None
        self.updated_at = None
        self.addresses = []
        self.settings = None

        self.setup_ui()
        self.update_user_info()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignCenter)

        left_side = QWidget()
        left_side.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}
            """
        )

        left_side_layout = QVBoxLayout(left_side)
        left_side_layout.setContentsMargins(0, 0, 0, 0)
        left_side_layout.setSpacing(10)
        left_side_layout.setAlignment(Qt.AlignTop)

        self.add_user_details(left_side_layout)
        self.add_addresses(left_side_layout)

        layout.addWidget(left_side)
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

    def update_user_info(self):
        if self.username:
            self.username_edit.setText(self.username)
        else:
            self.username_edit.setPlaceholderText("Create A Username")

        if self.created_at:
            self.created_at_display.setText(self.created_at)
        else:
            self.created_at_display.setPlaceholderText("01/01/0001 00:00")

        # doesn't show if the check in load_profile_info doesn't pass. doesn't need else clause
        if self.updated_at:
            self.updated_at_display.setText(self.updated_at)

        if not self.addresses:
            address_item = QListWidgetItem("No Addresses Currently Exist")
            self.addresses_box.addItem(address_item)
        
        else:
            for address in self.addresses:
                address_item = QListWidgetItem(address)
                
                self.addresses_box.addItem(address_item)

    def add_user_details(self, layout):
        user_details = QWidget()
        user_details.setStyleSheet(
            f"""
                QWidget {{
                    background-color: transparent;
                }}
            """
        )

        user_details_layout = QVBoxLayout(user_details)
        user_details_layout.setContentsMargins(10, 10, 10, 10)
        user_details_layout.setSpacing(10)
        user_details_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        title = QLabel("Profile")
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

        details_card = QWidget()
        details_card.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}
            """
        )

        details_card_layout = QVBoxLayout(details_card)
        details_card_layout.setContentsMargins(5, 5, 5, 5)
        details_card_layout.setSpacing(5)
        details_card_layout.setAlignment(Qt.AlignTop)

        username_details_row = QWidget()
        username_details_row.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}
            """
        )

        username_details_row_layout = QHBoxLayout(username_details_row)
        username_details_row_layout.setContentsMargins(0, 0, 0, 0)
        username_details_row_layout.setSpacing(10)
        username_details_row_layout.setAlignment(Qt.AlignCenter)

        username_label = QLabel("Username")
        username_label.setStyleSheet(
            f"""
                QLabel {{
                    font-style: italic;
                    font-size: 12px;
                    color: {self.color_theme['text_primary']};
                }}
            """
        )

        self.username_edit = QLineEdit()
        self.username_edit.setFixedWidth(250)
        self.username_edit.setAlignment(Qt.AlignRight)
        self.username_edit.setStyleSheet(
            f"""
                QLineEdit {{
                    border-bottom: 2px solid {self.color_theme['primary']};
                    color: {self.color_theme['text_primary']};
                    font-size: 12px;
                }}
            """
        )

        created_at_row = QWidget()
        created_at_row.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}
            """
        )

        created_at_row_layout = QHBoxLayout(created_at_row)
        created_at_row_layout.setContentsMargins(0, 0, 0, 0)
        created_at_row_layout.setSpacing(10)
        created_at_row_layout.setAlignment(Qt.AlignCenter)

        created_at_label = QLabel("Created On")
        created_at_label.setStyleSheet(
            f"""
                QLabel {{
                    font-style: italic;
                    font-size: 12px;
                    color: {self.color_theme['text_primary']};
                }}
            """
        )

        self.created_at_display = QLineEdit()
        self.created_at_display.setFixedWidth(250)
        self.created_at_display.setAlignment(Qt.AlignRight)
        self.created_at_display.setEnabled(False)
        self.created_at_display.setStyleSheet(
            f"""
                QLineEdit {{
                    border-bottom: 2px solid {self.color_theme['primary']};
                    color: {self.color_theme['text_primary']};
                    font-size: 12px;
                }}
            """
        )

        updated_at_row = QWidget()
        updated_at_row.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}
            """
        )

        updated_at_row_layout = QHBoxLayout(updated_at_row)
        updated_at_row_layout.setContentsMargins(0, 0, 0, 0)
        updated_at_row_layout.setSpacing(19)
        updated_at_row_layout.setAlignment(Qt.AlignCenter)

        updated_at_label = QLabel("Last Updated")
        updated_at_label.setStyleSheet(
            f"""
                QLabel {{
                    font-style: italic;
                    font-size: 12px;
                    color: {self.color_theme['text_primary']};
                }}
            """
        )

        self.updated_at_display = QLineEdit()
        self.updated_at_display.setFixedWidth(250)
        self.updated_at_display.setAlignment(Qt.AlignRight)
        self.updated_at_display.setEnabled(False)
        self.updated_at_display.setStyleSheet(
            f"""
                QLineEdit {{
                    border-bottom: 2px solid {self.color_theme['primary']};
                    color: {self.color_theme['text_primary']};
                    font-size: 12px;
                }}
            """
        )

        username_details_row_layout.addWidget(username_label)
        username_details_row_layout.addWidget(self.username_edit)

        created_at_row_layout.addWidget(created_at_label)
        created_at_row_layout.addWidget(self.created_at_display)

        updated_at_row_layout.addWidget(updated_at_label)
        updated_at_row_layout.addWidget(self.updated_at_display)

        details_card_layout.addWidget(username_details_row)
        details_card_layout.addWidget(created_at_row)

        if self.updated_at:
            details_card_layout.addWidget(updated_at_row)

        user_details_layout.addWidget(title)
        user_details_layout.addWidget(details_card, 1)
        user_details_layout.addStretch()

        layout.addWidget(user_details, 1)
        return layout
    
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