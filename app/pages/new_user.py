from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, 
    QStatusBar, QSlider
)

from PySide6.QtCore import Qt, QTimer


class NewUser(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("NewUser")

        self.color_theme = parent.color_theme
        self.json_engine = parent.json_engine
        self.parent_app = parent

        self.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}

                QWidget#half-container {{
                    border: none;
                }}

                QLabel#title {{
                    font-weight: bold;
                    font-style: italic;
                    font-size: 14px;
                    letter-spacing: 0.2em;
                    color: {self.color_theme['primary']};
                }}

                QLabel#sub-title {{
                    font-style: italic;
                    font-size: 14px;
                    letter-spacing: 0.2em;
                    color: {self.color_theme['primary']};
                }}

                QLabel#form-label {{
                    font-style: italic;
                    font-size: 12px;
                    color: {self.color_theme['text_primary']};
                    border: none;
                }}

                QLabel#description {{
                    border-left: 2px solid {self.color_theme['primary']};
                    border-radius: {self.color_theme['border_radius_small']};
                    background-color: {self.color_theme['surface_glass']};
                    padding: 5px;
                    font-size: 12px;
                }}

                QLineEdit#form-input {{
                    border-bottom: 2px solid {self.color_theme['primary']};
                    color: {self.color_theme['text_primary']};
                    font-size: 12px;
                }}

                QLineEdit#form-input:hover {{
                    background-color: {self.color_theme['surface_glass_hover']};
                }}

                QLineEdit#form-input:focus {{
                    background-color: {parent.color_theme['surface_glass']};
                }}

                QPushButton#ready-btn {{
                    border: 2px solid {self.color_theme['primary']};
                    border-radius: {self.color_theme['border_radius_small']};
                    background-color: transparent;
                    font-size: 10px;
                    color: {self.color_theme['text_primary']};
                    padding: 5px 12px;
                }}

                QPushButton#ready-btn:hover {{
                    background-color: {self.color_theme['surface_glass_hover']};
                }}
            """
        )

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Welcome to Skyloom!")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)

        bottom_half = QWidget()
        bottom_half.setObjectName("half-container")

        bottom_half_layout = QHBoxLayout(bottom_half)
        bottom_half_layout.setContentsMargins(0, 0, 0, 0)
        bottom_half_layout.setSpacing(50)
        bottom_half_layout.setAlignment(Qt.AlignCenter)

        left_side = QWidget()
        left_side.setFixedWidth(550)
        left_side.setObjectName("half-container")
        
        left_side_layout = QVBoxLayout(left_side)
        left_side_layout.setContentsMargins(10, 0, 10, 0)
        left_side_layout.setSpacing(50)
        left_side_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        description_one = QLabel(
            "Skyloom is a simple weather dashboard application designed to bring " \
            "you weather alerts and current weather predictions based off " \
            "<a href='https://openweathermap.org/api'>OpenWeather's</a> api " \
            "which is a free, open-source weather api."
        )
        description_one.setOpenExternalLinks(True)
        description_one.setObjectName("description")
        description_one.setWordWrap(True)
        description_one.setFixedHeight(150)
        description_one.setFixedWidth(450)

        description_two = QLabel(
            "All the data is controlled by you. From the data you input, to the place it " \
            "is stored, all happens on your device - no internet connection required for " \
            "data storage."
        )
        description_two.setObjectName("description")
        description_two.setWordWrap(True)
        description_two.setFixedHeight(150)
        description_two.setFixedWidth(450)

        description_three = QLabel(
            "All you \"create\" for your account is a username for a bit of " \
            "personalization! No emails, no phone numbers, no 2fa... Just you :)"
        )
        description_three.setObjectName("description")
        description_three.setWordWrap(True)
        description_three.setFixedHeight(150)
        description_three.setFixedWidth(450)

        right_side = QWidget()
        right_side.setFixedWidth(550)
        right_side.setObjectName("half-container")

        right_side_layout = QVBoxLayout(right_side)
        right_side_layout.setContentsMargins(10, 10, 20, 10)
        right_side_layout.setSpacing(15)
        right_side_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        ready_label = QLabel("Ready to get started???")
        ready_label.setAlignment(Qt.AlignCenter)
        ready_label.setObjectName("title")

        self.username_edit = QLineEdit()
        self.username_edit.setAlignment(Qt.AlignCenter)
        self.username_edit.setObjectName("form-input")
        self.username_edit.setPlaceholderText("Create A Username Here!")

        address_label = QLabel("Enter Your Address")
        address_label.setObjectName("sub-title")
        address_label.setAlignment(Qt.AlignCenter)

        self.street_edit = QLineEdit()
        self.street_edit.setObjectName("form-input")
        self.street_edit.setAlignment(Qt.AlignCenter)
        self.street_edit.setPlaceholderText("123 Example Lane")

        row_a = QWidget()
        row_a.setObjectName("half-container")

        row_a_layout = QHBoxLayout(row_a)
        row_a_layout.setContentsMargins(0, 0, 0, 0)
        row_a_layout.setSpacing(10)
        row_a_layout.setAlignment(Qt.AlignCenter)

        self.city_edit = QLineEdit()
        self.city_edit.setObjectName("form-input")
        self.city_edit.setAlignment(Qt.AlignCenter)
        self.city_edit.setPlaceholderText("Some City")

        self.state_edit = QLineEdit()
        self.state_edit.setObjectName("form-input")
        self.state_edit.setFixedWidth(70)
        self.state_edit.setAlignment(Qt.AlignCenter)
        self.state_edit.setPlaceholderText("ST")
        self.state_edit.setMaxLength(2)

        self.zip_edit = QLineEdit()
        self.zip_edit.setObjectName("form-input")
        self.zip_edit.setFixedWidth(100)
        self.zip_edit.setAlignment(Qt.AlignCenter)
        self.zip_edit.setPlaceholderText("12345")
        self.zip_edit.setMaxLength(5)

        settings_label = QLabel("Choose Your Settings")
        settings_label.setObjectName("sub-title")
        settings_label.setAlignment(Qt.AlignCenter)

        row1 = QWidget()
        row1.setObjectName("half-container")

        row1_layout = QHBoxLayout(row1)
        row1_layout.setContentsMargins(0, 0, 0, 0)
        row1_layout.setSpacing(10)
        row1_layout.setAlignment(Qt.AlignCenter)

        f_label = QLabel("Fahrenheit")
        f_label.setObjectName("form-label")
        f_label.setAlignment(Qt.AlignCenter)

        self.f_c_slider = QSlider(Qt.Horizontal)
        self.f_c_slider.setTickInterval(1)
        self.f_c_slider.setSliderPosition(1)
        self.f_c_slider.setMinimum(0)
        self.f_c_slider.setMaximum(2)
        self.f_c_slider.setFixedWidth(150)
        
        c_label = QLabel("Celcius")
        c_label.setObjectName("form-label")
        c_label.setAlignment(Qt.AlignCenter)

        row2 = QWidget()
        row2.setObjectName("half-container")

        row2_layout = QHBoxLayout(row2)
        row2_layout.setContentsMargins(0, 0, 0, 0)
        row2_layout.setSpacing(10)
        row2_layout.setAlignment(Qt.AlignCenter)

        mph_label = QLabel("MPH")
        mph_label.setToolTip("Miles Per Hour")
        mph_label.setObjectName("form-label")
        mph_label.setAlignment(Qt.AlignCenter)

        self.mph_kph_slider = QSlider(Qt.Horizontal)
        self.mph_kph_slider.setTickInterval(1)
        self.mph_kph_slider.setSliderPosition(1)
        self.mph_kph_slider.setMinimum(0)
        self.mph_kph_slider.setMaximum(2)
        self.mph_kph_slider.setFixedWidth(150)

        kph_label = QLabel("KPH")
        kph_label.setToolTip("Kilometers Per Hour")
        kph_label.setObjectName("form-label")
        kph_label.setAlignment(Qt.AlignCenter)

        row3 = QWidget()
        row3.setObjectName("half-container")

        row3_layout = QHBoxLayout(row3)
        row3_layout.setContentsMargins(0, 0, 0, 0)
        row3_layout.setSpacing(10)
        row3_layout.setAlignment(Qt.AlignCenter)

        mb_label = QLabel("MB")
        mb_label.setToolTip("Millibars")
        mb_label.setObjectName("form-label")
        mb_label.setAlignment(Qt.AlignCenter)

        self.mb_in_slider = QSlider(Qt.Horizontal)
        self.mb_in_slider.setTickInterval(1)
        self.mb_in_slider.setMinimum(0)
        self.mb_in_slider.setMaximum(2)
        self.mb_in_slider.setSliderPosition(1)
        self.mb_in_slider.setFixedWidth(150)

        in_label = QLabel("IN")
        in_label.setToolTip("Inches of Mercury")
        in_label.setObjectName("form-label")
        in_label.setAlignment(Qt.AlignCenter)

        row4 = QWidget()
        row4.setObjectName("half-container")

        row4_layout = QHBoxLayout(row4)
        row4_layout.setContentsMargins(0, 0, 0, 0)
        row4_layout.setSpacing(10)
        row4_layout.setAlignment(Qt.AlignCenter)

        miles_label = QLabel("MI")
        miles_label.setToolTip("Miles")
        miles_label.setObjectName("form-label")
        miles_label.setAlignment(Qt.AlignCenter)

        self.mi_km_slider = QSlider(Qt.Horizontal)
        self.mi_km_slider.setTickInterval(1)
        self.mi_km_slider.setMinimum(0)
        self.mi_km_slider.setMaximum(2)
        self.mi_km_slider.setSliderPosition(1)
        self.mi_km_slider.setFixedWidth(150)

        kilo_label = QLabel("KM")
        kilo_label.setToolTip("Kilometers")
        kilo_label.setObjectName("form-label")
        kilo_label.setAlignment(Qt.AlignCenter)

        read_write_label = QLabel("Read/Write Permissions")
        read_write_label.setObjectName("sub-title")
        read_write_label.setAlignment(Qt.AlignCenter)

        disclaimer_label = QLabel(
            "This application requires read/write permissions from you " \
            "in order to create your profile and store your information since " \
            "the information is stored on your device locally. As the developers, " \
            "we cannot, in good faith, create a program that handles physical action " \
            "to your computer without your consent"
        )
        disclaimer_label.setStyleSheet(f"QLabel {{ font-size: 10px; color: {self.color_theme['text_primary']}; }}")
        disclaimer_label.setAlignment(Qt.AlignCenter)
        disclaimer_label.setFixedHeight(70)
        disclaimer_label.setWordWrap(True)

        agree_label = QLabel("Do You Agree?\nNote: This application cannot run without this permission")
        agree_label.setAlignment(Qt.AlignCenter)
        agree_label.setStyleSheet(f"QLabel {{ font-size: 10px; color: {self.color_theme['text_primary']}; }}")

        agree_row = QWidget()
        agree_row.setObjectName("half-container")

        agree_row_layout = QHBoxLayout(agree_row)
        agree_row_layout.setContentsMargins(0, 0, 0, 0)
        agree_row_layout.setSpacing(10)
        agree_row_layout.setAlignment(Qt.AlignCenter)

        yes = QLabel("Yes")
        yes.setObjectName("form-label")
        yes.setAlignment(Qt.AlignCenter)

        self.agree_slider = QSlider(Qt.Horizontal)
        self.agree_slider.setTickInterval(1)
        self.agree_slider.setMinimum(0)
        self.agree_slider.setMaximum(2)
        self.agree_slider.setSliderPosition(1)
        self.agree_slider.setFixedWidth(150)

        no = QLabel("No")
        no.setObjectName("form-label")
        no.setAlignment(Qt.AlignCenter)

        ready_btn = QPushButton("Let's Go!")
        ready_btn.setObjectName("ready-btn")
        ready_btn.clicked.connect(self.create_user)

        self.status_bar = QStatusBar()

        left_side_layout.addWidget(description_one)
        left_side_layout.addWidget(description_two)
        left_side_layout.addWidget(description_three)

        row_a_layout.addWidget(self.city_edit)
        row_a_layout.addWidget(self.state_edit)
        row_a_layout.addWidget(self.zip_edit)

        row1_layout.addWidget(f_label)
        row1_layout.addWidget(self.f_c_slider)
        row1_layout.addWidget(c_label)

        row2_layout.addWidget(mph_label)
        row2_layout.addWidget(self.mph_kph_slider)
        row2_layout.addWidget(kph_label)

        row3_layout.addWidget(mb_label)
        row3_layout.addWidget(self.mb_in_slider)
        row3_layout.addWidget(in_label)

        row4_layout.addWidget(miles_label)
        row4_layout.addWidget(self.mi_km_slider)
        row4_layout.addWidget(kilo_label)

        agree_row_layout.addWidget(yes)
        agree_row_layout.addWidget(self.agree_slider)
        agree_row_layout.addWidget(no)

        right_side_layout.addWidget(ready_label)
        right_side_layout.addWidget(self.username_edit)
        right_side_layout.addWidget(self.street_edit)
        right_side_layout.addWidget(row_a)
        right_side_layout.addWidget(settings_label)
        right_side_layout.addWidget(row1)
        right_side_layout.addWidget(row2)
        right_side_layout.addWidget(row3)
        right_side_layout.addWidget(row4)
        right_side_layout.addWidget(read_write_label)
        right_side_layout.addWidget(disclaimer_label)
        right_side_layout.addWidget(agree_label)
        right_side_layout.addWidget(agree_row)
        right_side_layout.addWidget(ready_btn)

        bottom_half_layout.addWidget(left_side, 1)
        bottom_half_layout.addWidget(right_side, 1)

        layout.addWidget(title)
        layout.addWidget(bottom_half, 2)
        layout.addWidget(self.status_bar)

        layout.addStretch()

    def handle_error_success(self, msg: str, is_error: bool = True):
        if is_error:
            self.status_bar.setStyleSheet(
                f"""
                    QStatusBar {{
                        font-size: 12px;
                        font-weight: bold;
                        font-style: italic;
                        color: black;
                        background-color: {self.color_theme['error']};
                        letter-spacing: 0.2em;
                        word-spacing: 0.2em;
                    }}
                """
            )
        else:
            self.status_bar.setStyleSheet(
                f"""

                    QStatusBar {{
                        font-size: 12px;
                        font-weight: bold;
                        font-style: italic;
                        color: black;
                        background-color: {self.color_theme['success']};
                        letter-spacing: 0.2em;
                        word-spacing: 0.2em;
                    }}
                """
            )

        self.status_bar.showMessage(msg)

        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.reset_status_bar)
        self.timer.start()

    def reset_status_bar(self):
        self.status_bar.clearMessage()
        self.status_bar.setStyleSheet("")

    def create_user(self):        
        new_user = {
            "read_write": False,
            "username": "",
            "addresses": [],
            "settings": {
                "f_c": "",
                "mph_kph": "",
                "mb_in": "",
                "mi_km": ""
            }
        }

        username = self.username_edit.text().strip()
        street = self.street_edit.text().strip()
        city = self.city_edit.text().strip()
        state = self.state_edit.text().strip()
        zip = self.zip_edit.text().strip()

        f_c_value = self.f_c_slider.sliderPosition()
        mph_kph_value = self.mph_kph_slider.sliderPosition()
        mb_in_value = self.mb_in_slider.sliderPosition()
        mi_km_value = self.mi_km_slider.sliderPosition()

        if not username and not street and not city and not state and not zip:
            return self.handle_error_success("All Inputs Are Required")
        
        if not username:
            return self.handle_error_success("Username is Required")
        
        if not street:
            return self.handle_error_success("Street Address is Required")
        
        if not city:
            return self.handle_error_success("City is Required")
        
        if not state:
            return self.handle_error_success("State/Province is Required")
        
        if not zip:
            return self.handle_error_success("Zip/Postal Code is Required")
        
        if f_c_value == 1 and mph_kph_value == 1 and mb_in_value == 1 and mi_km_value == 1:
            return self.handle_error_success("Invalid Settings. Please Select One of Each")
        
        if f_c_value == 1:
            return self.handle_error_success("Please Select A Temperature Reading Setting")
        
        if mph_kph_value == 1:
            return self.handle_error_success("Please Select A Speed Reading Setting")
        
        if mb_in_value == 1:
            return self.handle_error_success("Please Select A Pressure Reading Setting")
        
        if mi_km_value == 1:
            return self.handle_error_success("Please Select A Distance Reading Setting")
        
        if self.agree_slider.sliderPosition() in [1, 2]:
            return self.handle_error_success(
                "You Denied The Agreement. This app can't run without this agreement"
            )
        
        new_user["read_write"] = True if self.agree_slider.sliderPosition() == 0 else False
        new_user["username"] = username
        new_user["addresses"].append(', '.join([street, city, state, zip]))

        if f_c_value == 0:
            new_user["settings"]["f_c"] = "f"
        elif f_c_value == 2:
            new_user["settings"]["f_c"] = "c"
        else:
            return self.handle_error_success("Invalid Temperature Reading Setting")
        
        if mph_kph_value == 0:
            new_user["settings"]["mph_kph"] = "mph"
        elif mph_kph_value == 2:
            new_user["settings"]["mph_kph"] = "kph"
        else:
            return self.handle_error_success("Invalid Speed Readi   ng Setting")
        
        if mb_in_value == 0:
            new_user["settings"]["mb_in"] = "mb"
        elif mb_in_value == 2:
            new_user["settings"]["mb_in"] = "in"
        else:
            return self.handle_error_success("Invalid Pressure Reading Setting")
        
        if mi_km_value == 0:
            new_user["settings"]["mi_km"] = "mi"
        elif mi_km_value == 2:
            new_user["settings"]["mi_km"] = "km"
        else:
            return self.handle_error_success("Invalid Distance Reading Setting")

        try:
            self.json_engine.create_user_profile(new_user)
            self.parent_app.on_user_created()
            self.handle_error_success("User Created Succesfully. Reloading Application... Please Wait...", False)

        except Exception as e:
            print(e)
            return self.handle_error_success("Failed to Create New User")