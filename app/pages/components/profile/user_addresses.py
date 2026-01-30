from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton,
    QLineEdit, QLabel
)

from PySide6.QtCore import Qt


class UserAddresses(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.color_theme = parent.color_theme
        self.user = parent.user

        self.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}

                QWidget#address-edit {{
                    border: none;
                }}

                QLabel#title {{
                    font-weight: bold;
                    font-style: italic;
                    font-size: 14px;
                    letter-spacing: 0.2em;
                    color: {self.color_theme['primary']};
                }}

                QLabel#form-label {{
                    font-style: italic;
                    font-size: 12px;
                    color: {self.color_theme['text_primary']};
                    border: none;
                }}

                QLineEdit#form-input {{
                    border-bottom: 2px solid {self.color_theme['primary']};
                    color: {self.color_theme['text_primary']};
                    font-size: 12px;
                }}

                QLineEdit#form-input:hover {{
                    background-color: {self.color_theme['surface_glass_hover']};
                }}

                QLineEdit#form-input:focus {{
                    background-color: {parent.color_theme['surface_glass']};
                }}

                QPushButton#update-btn {{
                    border: 2px solid {self.color_theme['primary']};
                    border-radius: {self.color_theme['border_radius_small']};
                    background-color: transparent;
                    font-size: 10px;
                    color: {self.color_theme['text_primary']};
                }}

                QPushButton#update-btn:hover {{
                    background-color: {self.color_theme['surface_glass_hover']};
                }}

                QListWidget#address-card {{
                    border: 2px solid {self.color_theme['primary']};
                    border-radius: {self.color_theme['border_radius_small']};
                    background-color: transparent;
                }}

                QListWidget#address-card::item {{
                    color: {self.color_theme['text_primary']};
                }}

                QListWidget#address-card::item:hover {{
                    background-color: {self.color_theme['surface_glass_hover']};
                }}

                QListWidget#address-card::item:selected {{
                    background-color: {self.color_theme['surface_glass_hover']};
                }}
            """
        )

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        title = QLabel("Current Addresses")
        title.setObjectName("title")

        address_card = QListWidget()
        address_card.setObjectName("address-card")

        edit_row = QWidget()
        edit_row.setObjectName("address-edit")

        edit_row_layout = QHBoxLayout(edit_row)
        edit_row_layout.setContentsMargins(0, 0, 0, 0)
        edit_row_layout.setSpacing(10)
        edit_row_layout.setAlignment(Qt.AlignCenter)

        edit_label = QLabel("Add/Edit")
        edit_label.setObjectName("form-label")
        
        self.address_edit = QLineEdit()
        self.address_edit.setObjectName("form-input")
        self.address_edit.setFixedWidth(250)
        self.address_edit.setAlignment(Qt.AlignRight)
        self.address_edit.returnPressed.connect(self.save_address)

        update_btn = QPushButton("Submit")
        update_btn.setObjectName("update-btn")
        update_btn.clicked.connect(self.save_address)
        update_btn.setFixedSize(60, 20)

        edit_row_layout.addWidget(edit_label)
        edit_row_layout.addWidget(self.address_edit)
        edit_row_layout.addWidget(update_btn)

        layout.addWidget(title)
        layout.addWidget(address_card, 2)
        layout.addWidget(edit_row)

    def save_address(self):
        # search for address by id
        # update address if exists
        # save address to list of addresses if not
        pass

    def load_user(self):
        if self.user['addresses']:
            pass