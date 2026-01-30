from qfluentwidgets import (
    MSFluentWindow, FluentIcon as fi,
    setTheme, Theme, setThemeColor, 
    NavigationItemPosition
)

from .pages.dashboard import Dashboard
from .pages.profile import Profile
from .pages.new_user import NewUser
from .pages.about import About
from .pages.support import Support


class Skyloom(MSFluentWindow):
    def __init__(self, color_theme, json_engine, weather_engine):
        super().__init__()

        self.color_theme = color_theme
        self.json_engine = json_engine
        self.weather_engine = weather_engine

        self.user = self.json_engine.get_user_profile()

        self.dashboard = Dashboard(self)
        self.profile = Profile(self)
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
        self.user = self.json_engine.get_user_profile()
        
        if not self.user or not self.user.get("read_write", False):
            self.addSubInterface(self.new_user, fi.PEOPLE, "NewUser", position=NavigationItemPosition.TOP)
            self.switchTo(self.new_user)
        else:
            self.addSubInterface(self.profile, fi.PEOPLE, "Profile", position=NavigationItemPosition.TOP)
            self.addSubInterface(self.dashboard, fi.HOME, "Dashboard", position=NavigationItemPosition.TOP)
            self.switchTo(self.dashboard)

        self.addSubInterface(self.about, fi.INFO, "About", position=NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.support, fi.ADD, "Support", position=NavigationItemPosition.BOTTOM)

    def on_user_created(self):
        self.user = self.json_engine.get_user_profile()
        
        for widget in self.findChildren(type(self.new_user)):
            if hasattr(widget, 'objectName') and widget.objectName() in ["Dashboard", "Profile", "NewUser", "About", "Support"]:
                self.navigationInterface.removeWidget(widget)
        
        self.init_navigation()
        self.switchTo(0)