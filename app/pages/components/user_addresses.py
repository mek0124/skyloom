from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton,
    QLineEdit
)


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

                QLabel#title {{
                    font-weight: bold;
                    font-style: italic;
                    font-size: 14px;
                    letter-spacing: 0.2em;
                    color: {parent.color_theme['primary']};
                }}

                QLabel#form-label {{
                    font-style: italic;
                    font-size: 12px;
                    color: {parent.color_theme['text_primary']};
                }}

                QLineEdit#form-input {{
                    border-bottom: 2px solid {parent.color_theme['primary']};
                    color: {parent.color_theme['text_primary']};
                    font-size: 12px;
                }}

                QLineEdit#form-input:hover {{
                    background-color: {parent.color_theme['surface_glass_hover']};
                }}

                QLineEdit#form-input:focus {{
                    background-color: {parent.color_theme['surface_glass']};
                }}

                QPushButton#update-btn {{
                    border: 2px solid {parent.color_theme['primary']};
                    border-radius: {parent.color_theme['border_radius_medium']};
                    background-color: transparent;
                    font-size: 10px;
                    color: {parent.color_theme['text_primary']};
                }}

                QPushButton#update-btn:hover {{
                    background-color: {parent.color_theme['surface_glass_hover']};
                }}
            """
        )

        self.setup_ui()

    def setup_ui(self):
        pass