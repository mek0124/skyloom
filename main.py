from PySide6.QtWidgets import QApplication, QMessageBox
from pathlib import Path

from app.app import Skyloom
from setup.app import SkyloomNewUser

from core.color_theme import COLOR_THEME
from core.json import JsonEngine
from core.weather import WeatherEngine

import sys


def run():
    app = QApplication(sys.argv)

    root_dir = Path(__file__).parent
    storage_dir = root_dir / "core" / "storage"
    storage_dir.mkdir(parents=True, exist_ok=True)

    weather_engine = WeatherEngine()
    json_engine = JsonEngine(root_dir)
    existing_user = json_engine.get_user_profile()

    if existing_user is None or not existing_user.get("username"):
        window = SkyloomNewUser(COLOR_THEME, json_engine)
        window.setWindowTitle("Skyloom - New User")
        run()
        
    else:
        window = Skyloom(existing_user, COLOR_THEME, root_dir, json_engine, weather_engine)
        window.setWindowTitle("Skyloom")

    window.showMaximized()
    sys.exit(app.exec())


if __name__ == '__main__':
    run()