from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit
)

from PySide6.QtCore import Qt, QTimer

from .components.main_display import MainDisplay
from .components.warning_strip import WarningStrip


class Dashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Dashboard")

        self.theme = parent.color_theme
        self.color_theme = parent.color_theme
        self.json_engine = parent.json_engine
        self.user = parent.user
        self.weather_engine = parent.weather_engine

        self.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}

                QWidget#title-row {{
                    border: none;
                }}

                QLabel#title {{
                    font-weight: bold;
                    font-style: italic;
                    font-size: 14px;
                    color: {self.color_theme['primary']};
                    letter-spacing: 0.3em;
                }}

                QLineEdit#form-input {{
                    border-bottom: 2px solid {self.color_theme['primary']};
                    color: {self.color_theme['text_primary']};
                    font-size: 12px;
                }}
            """
        )

        self.is_loading = False
        self.warnings = None
        self.current_weather = None
        self.main_display = None
        
        self.setup_ui()
        self.load_dashboard()

        self.timer = QTimer()
        self.timer.setInterval(3600)
        self.timer.timeout.connect(self.load_dashboard)
        self.timer.start()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignCenter)

        title_row = QWidget()
        title_row.setObjectName("title-row")

        title_row_layout = QHBoxLayout(title_row)
        title_row_layout.setContentsMargins(0, 0, 0, 0)
        title_row_layout.setSpacing(0)
        title_row_layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Weather Conditions")
        title.setObjectName("title")

        self.user_location = QLineEdit()
        self.user_location.setAlignment(Qt.AlignRight)
        self.user_location.returnPressed.connect(self.load_dashboard)
        self.user_location.setObjectName("form-input")

        title_row_layout.addWidget(title)
        title_row_layout.addWidget(self.user_location)

        warning_strip = WarningStrip(self)
        self.main_display = MainDisplay(self)
        
        layout.addWidget(title_row)
        layout.addWidget(warning_strip)
        layout.addWidget(self.main_display)
        layout.addStretch()

    def load_dashboard(self):
        if self.user is None or not self.user or not hasattr(self.user, "settings"):
            return
        
        weather_response = self.weather_engine.get_current_weather(self.user['settings']['alerts'])
        response_display = self.weather_engine.display_response(weather_response, self.user['settings'])

        if self.main_display:
            self.main_display.update_weather(response_display)
        
        # Also update warnings if needed
        # self.update_warnings()