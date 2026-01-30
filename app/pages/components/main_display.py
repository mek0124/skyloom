from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QGridLayout
)

from PySide6.QtCore import Qt


class MainDisplay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.color_theme = parent.color_theme
        self.parent_layout = parent.layout()

        self.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}

                QWidget#main-container {{
                    border: none;
                }}

                QWidget#widget-card {{
                    border: 2px solid {self.color_theme['primary']};
                    border-radius: {self.color_theme['border_radius_medium']};
                    background-color: {self.color_theme['secondary']};
                }}

                QWidget#widget-card-row {{
                    border: none;
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
            """
        )
        
        self.setup_ui()

    def setup_ui(self):
        main_display = QWidget()
        main_display.setObjectName("main-container")

        main_display_layout = QGridLayout(main_display)
        main_display_layout.setContentsMargins(10, 10, 10, 10)
        main_display_layout.setSpacing(0)
        main_display_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        current_widget = QWidget()
        current_widget.setFixedSize(180, 150)
        current_widget.setObjectName("widget-card")

        current_widget_layout = QVBoxLayout(current_widget)
        current_widget_layout.setContentsMargins(10, 10, 10, 10)
        current_widget_layout.setSpacing(10)
        current_widget_layout.setAlignment(Qt.AlignTop)

        last_updated_row = QWidget()
        last_updated_row.setObjectName("widget-card-row")

        last_updated_row_layout = QHBoxLayout(last_updated_row)
        last_updated_row_layout.setContentsMargins(0, 0, 0, 0)
        last_updated_row_layout.setSpacing(0)
        last_updated_row_layout.setAlignment(Qt.AlignCenter)

        last_updated_label = QLabel("Last Updated")
        last_updated_label.setObjectName("form-label")

        self.last_updated_display = QLabel("Loading...")
        self.last_updated_display.setAlignment(Qt.AlignRight)
        self.last_updated_display.setObjectName("form-input")

        current_temp_row = QWidget()
        current_temp_row.setObjectName("widget-card-row")

        current_temp_row_layout = QHBoxLayout(current_temp_row)
        current_temp_row_layout.setContentsMargins(0, 0, 0, 0)
        current_temp_row_layout.setSpacing(0)
        current_temp_row_layout.setAlignment(Qt.AlignCenter)

        current_temp_label = QLabel("Temperature")
        current_temp_label.setObjectName("form-label")

        self.current_temp_display = QLabel("Loading...")
        self.current_temp_display.setAlignment(Qt.AlignRight)
        self.current_temp_display.setObjectName("form-input")

        feels_like_row = QWidget()
        feels_like_row.setObjectName("widget-card-row")

        feels_like_row_layout = QHBoxLayout(feels_like_row)
        feels_like_row_layout.setContentsMargins(0, 0, 0, 0)
        feels_like_row_layout.setSpacing(0)
        feels_like_row_layout.setAlignment(Qt.AlignCenter)

        feels_like_label = QLabel("Feels Like")
        feels_like_label.setObjectName("form-label")

        self.feels_like_display = QLabel("Loading...")
        self.feels_like_display.setAlignment(Qt.AlignRight)
        self.feels_like_display.setObjectName("form-input")

        current_condition_row = QWidget()
        current_condition_row.setObjectName("widget-card-row")

        current_condition_row_layout = QHBoxLayout(current_condition_row)
        current_condition_row_layout.setContentsMargins(0, 0, 0, 0)
        current_condition_row_layout.setSpacing(0)
        current_condition_row_layout.setAlignment(Qt.AlignCenter)

        current_condition_label = QLabel("Condition")
        current_condition_label.setObjectName("form-label")

        self.current_condition_display = QLabel("Loading...")
        self.current_condition_display.setAlignment(Qt.AlignRight)
        self.current_condition_display.setObjectName("form-input")

        last_updated_row_layout.addWidget(last_updated_label)
        last_updated_row_layout.addWidget(self.last_updated_display, 1)

        feels_like_row_layout.addWidget(feels_like_label)
        feels_like_row_layout.addWidget(self.feels_like_display, 1)

        current_temp_row_layout.addWidget(current_temp_label)
        current_temp_row_layout.addWidget(self.current_temp_display, 1)

        current_condition_row_layout.addWidget(current_condition_label)
        current_condition_row_layout.addWidget(self.current_condition_display, 1)

        current_widget_layout.addWidget(last_updated_row)
        current_widget_layout.addWidget(feels_like_row)
        current_widget_layout.addWidget(current_temp_row)
        current_widget_layout.addWidget(current_condition_row)

        main_display_layout.addWidget(current_widget, 0, 0)

        self.parent_layout.addWidget(main_display)

    def update_weather(self, weather):
        self.last_updated_display.setText(str(weather["last_updated"]))
        self.feels_like_display.setText(str(weather["feels_like"]))
        self.current_temp_display.setText(str(weather["temperature"]))
        self.current_condition_display.setText(str(weather["condition"]))