from qfluentwidgets import (
    MSFluentWindow, FluentIcon as fi,
    setTheme, Theme, setThemeColor
)

from app.pages.dashboard import Dashboard
from app.pages.profile import Profile


class Skyloom(MSFluentWindow):
    def __init__(self, user, color_theme, root_dir, db):
        super().__init__()

        self.user = user
        self.color_theme = color_theme
        self.root_dir = root_dir
        self.db = db

        self.dashboard = Dashboard(self)
        self.profile = Profile(self)

        self.apply_app_styles()
        self.init_navigation()

    def apply_app_styles(self):
        setTheme(Theme.DARK)
        setThemeColor(self.color_theme['primary'])
        self.setStyleSheet(
            f"""
                QMainWindow {{
                    background-color: {self.color_theme['background']};
                }}
            """
        )

    def init_navigation(self):
        self.addSubInterface(self.profile, fi.PEOPLE, "Profile")
        self.addSubInterface(self.dashboard, fi.HOME, "Dashboard")
