from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton
)

from PySide6.QtCore import Qt, QTimer
from dotenv import load_dotenv

from .components.main_display import MainDisplay
from .components.warning_strip import WarningStrip

from ..utils.color_theme import COLOR_THEME as theme
from ..utils.weather import get_current_weather, build_display

import os


load_dotenv()


class Dashboard(QWidget):
    def __init__(self, theme, parent=None):
        super().__init__(parent)
        self.setObjectName("Dashboard")

        self.root_dir = parent.root_dir
        self.theme = theme

        self.is_loading = False
        self.warnings = None
        self.current_weather = None
        self.main_display = None
        self.user_settings = {
            "f_c": "f",
            "mph_kph": "mph",
            "km_mi": "mi",
            "mb_in": "mb"
        }
        
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
        layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        title_row = QWidget()
        title_row.setStyleSheet("QWidget {{ border: none; }}")

        title_row_layout = QHBoxLayout(title_row)
        title_row_layout.setContentsMargins(0, 0, 0, 0)
        title_row_layout.setSpacing(150)
        title_row_layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Weather Conditions")
        title.setStyleSheet(
            f"""
                QLabel {{
                    color: {self.theme['primary']};
                    font-weight: bold;
                    font-style: italic;
                    font-size: 14px;
                    letter-spacing: 0.3em;
                }}
            """
        )

        user_location = QLabel()
        user_location.setAlignment(Qt.AlignRight)
        user_location.setStyleSheet(
            f"""
                QLabel {{
                    color: {self.theme['text_primary']};
                }}
            """
        )

        title_row_layout.addWidget(title)
        title_row_layout.addWidget(user_location)

        layout.addWidget(title_row)

        warning_strip = WarningStrip(theme, self.warnings, self)
        self.main_display = MainDisplay(theme, None, self)
        
        layout.addWidget(warning_strip)
        layout.addWidget(self.main_display)
        layout.addStretch()

    def load_dashboard(self):
        weather_response = get_current_weather()
        response_display = build_display(weather_response, self.user_settings)

        if self.main_display:
            self.main_display.update_weather(response_display)
        
        # Also update warnings if needed
        # self.update_warnings()