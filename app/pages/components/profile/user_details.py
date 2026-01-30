from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton
)

from PySide6.QtCore import Qt


class UserDetails(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.user = parent.user
        self.color_theme = parent.color_theme

        self.username = None
        self.created_at = None
        self.updated_at = None

        self.setStyleSheet(
            f"""
                QWidget {{ 
                    border: none; 
                }}

                QWidget#details-card {{
                    border: none;
                }}

                QWidget#data-row {{
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
                    background-color: {self.color_theme['surface_glass']};
                }}

                QPushButton#update-btn {{
                    border: 2px solid {self.color_theme['primary']};
                    border-radius: {self.color_theme['border_radius_medium']};
                    background-color: transparent;
                    font-size: 10px;
                    color: {self.color_theme['text_primary']};
                }}

                QPushButton#update-btn:hover {{
                    background-color: {self.color_theme['surface_glass_hover']};
                }}
            """
        )

        self.setup_ui()
        self.load_user_info()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        title = QLabel("Profile Details")
        title.setObjectName("title")

        details_card = QWidget()
        details_card.setObjectName("details-card")

        details_card_layout = QVBoxLayout(details_card)
        details_card_layout.setContentsMargins(5, 5, 5, 5)
        details_card_layout.setSpacing(5)
        details_card_layout.setAlignment(Qt.AlignTop)

        username_row = QWidget()
        username_row.setObjectName("data-row")

        username_row_layout = QHBoxLayout(username_row)
        username_row_layout.setContentsMargins(0, 0, 0, 0)
        username_row_layout.setSpacing(10)
        username_row_layout.setAlignment(Qt.AlignCenter)

        username_label = QLabel("Username")
        username_label.setObjectName("form-label")

        self.username_edit = QLineEdit()
        self.username_edit.setFixedWidth(250)
        self.username_edit.setObjectName("form-input")
        self.username_edit.setAlignment(Qt.AlignRight)

        created_at_row = QWidget()
        created_at_row.setObjectName("data-row")

        created_at_row_layout = QHBoxLayout(created_at_row)
        created_at_row_layout.setContentsMargins(0, 0, 0, 0)
        created_at_row_layout.setSpacing(10)
        created_at_row_layout.setAlignment(Qt.AlignCenter)

        created_at_label = QLabel("Created On")
        created_at_label.setObjectName("form-label")

        self.created_at_display = QLineEdit()
        self.created_at_display.setObjectName("form-input")
        self.created_at_display.setFixedWidth(250)
        self.created_at_display.setEnabled(False)
        self.created_at_display.setAlignment(Qt.AlignRight)

        updated_at_row = QWidget()
        updated_at_row.setObjectName("data-row")

        updated_at_row_layout = QHBoxLayout(updated_at_row)
        updated_at_row_layout.setContentsMargins(0, 0, 0, 0)
        updated_at_row_layout.setSpacing(10)
        updated_at_row_layout.setAlignment(Qt.AlignCenter)

        updated_at_label = QLabel("Last Updated")
        updated_at_label.setObjectName("form-label")

        self.updated_at_display = QLineEdit()
        self.updated_at_display.setObjectName("form-input")
        self.updated_at_display.setFixedWidth(250)
        self.updated_at_display.setEnabled(False)
        self.updated_at_display.setAlignment(Qt.AlignRight)

        button_row = QWidget()
        button_row.setObjectName("data-row")

        button_row_layout = QHBoxLayout(button_row)
        button_row_layout.setContentsMargins(5, 5, 5, 5)
        button_row_layout.setSpacing(0)
        button_row_layout.setAlignment(Qt.AlignRight)

        update_btn = QPushButton("Create" if not self.user else "Update")
        update_btn.setObjectName("update-btn")
        update_btn.clicked.connect(self.update_user_info)
        update_btn.setFixedSize(80, 30)

        username_row_layout.addWidget(username_label)
        username_row_layout.addWidget(self.username_edit)

        created_at_row_layout.addWidget(created_at_label)
        created_at_row_layout.addWidget(self.created_at_display)

        if self.updated_at:
            updated_at_row_layout.addWidget(updated_at_label)
            updated_at_row_layout.addWidget(self.updated_at_display)

        button_row_layout.addWidget(update_btn)

        layout.addWidget(title)
        layout.addWidget(username_row)
        layout.addWidget(created_at_row)
        layout.addWidget(updated_at_row)
        layout.addWidget(button_row)

    def update_user_info(self):
        pass

    def load_user_info(self):
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