from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QPixmap
from pathlib import Path

from app.app import Skyloom

from app.utils.color_theme import COLOR_THEME
from app.utils.json import JsonEngine
from app.utils.weather import WeatherEngine

import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)

    root_dir = Path(__file__).parent
    storage_dir = root_dir / "app" / "storage"
    storage_dir.mkdir(parents=True, exist_ok=True)

    weather_engine = WeatherEngine()
    json_engine = JsonEngine(root_dir)
    
    window = Skyloom(COLOR_THEME, json_engine, weather_engine)
    window.setWindowTitle("Skyloom")
    
    icon = QPixmap("./app/assets/icon.jpeg")
    window.setWindowIcon(icon)

    window.showMaximized()

    sys.exit(app.exec())