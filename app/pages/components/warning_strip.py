from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer


class WarningStrip(QWidget):
    def __init__(self, theme, warnings, parent=None):
        super().__init__(parent)

        self.theme = theme
        self.parent_layout = parent.layout()
        self.warnings = warnings if warnings else []
        self.current_index = 0

        self.setup_ui()

    def setup_ui(self):
        warning_container = QWidget()
        warning_container.setStyleSheet("QWidget {{ border: none; }}")

        warning_container_layout = QVBoxLayout(warning_container)
        warning_container_layout.setContentsMargins(0, 0, 0, 0)
        warning_container_layout.setSpacing(0)
        warning_container_layout.setAlignment(Qt.AlignCenter)

        self.warning_label = QLabel("")
        self.warning_label.setAlignment(Qt.AlignCenter)
        self.warning_label.setStyleSheet(
            f"""
                QLabel {{
                    color: {self.theme['text_primary']};
                }}
            """
        )

        warning_container_layout.addWidget(self.warning_label)
        self.parent_layout.addWidget(warning_container)

    def show_next_message(self):
        if not self.warnings:
            return

        self.warning_label.setText(self.warnings[self.current_index])
        self.current_index = (self.current_index + 1) % len(self.warnings)