from qfluentwidgets import (
    MSFluentWindow, FluentIcon as fi,
    setTheme, Theme, setThemeColor
)

from .pages.new_user import NewUser
from .pages.about import About
from .pages.support import Support


class SkyloomNewUser(MSFluentWindow):
    def __init__(self, color_theme, json_engine):
        super().__init__()

        self.color_theme = color_theme
        self.json_engine = json_engine
        self.user_created = False

        self.new_user = NewUser(self)
        self.about = About(self)
        self.support = Support(self)

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
        self.addSubInterface(self.new_user, fi.PEOPLE, "NewUser")
        self.addSubInterface(self.about, fi.INFO, "About")
        self.addSubInterface(self.support, fi.ADD, "Support")