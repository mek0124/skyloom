from qfluentwidgets import (
    MSFluentWindow, FluentIcon, Theme,
    setTheme, setThemeColor, 
)

from .pages.dashboard import Dashboard
from .utils.color_theme import COLOR_THEME as theme


class Skyloom(MSFluentWindow):
    def __init__(self, root_dir):
        super().__init__()

        self.root_dir = root_dir
        self.theme = theme
        self.dashboard = Dashboard(self.theme, self)

        self.set_app_theme()
        self.init_navigation()

    def set_app_theme(self):
        setTheme(Theme.DARK)
        setThemeColor(theme['primary'])

        self.setStyleSheet(
            f"""
                QMainWindow {{
                    background-color: {theme['background']};
                }}
            """
        )

    def init_navigation(self):
        self.addSubInterface(self.dashboard, FluentIcon.HOME, "Dashboard")

    def closeEvent(self, event):
        event.accept()