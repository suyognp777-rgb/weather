import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class wapp(QWidget):

    def __init__(self):
        super().__init__()

        self.city_label = QLabel("enter your location:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("GET WEATHER", self)

        # Empty labels at first
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.get_weather_button.clicked.connect(self.getw)

    def getw(self):

        api = "d1742ca3f88f6069d21e61f2f02291e9"

        city = self.city_input.text()

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"

        try:
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            self.displayw(data)

        except requests.exceptions.HTTPError:
            print(response.status_code)

    def displayw(self, data):

        temperature = data["main"]["temp"]
        weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
    #set text to display it "label for  reserve and put text inside the window" "set text to change whats written in that box"
        self.temperature_label.setText(str(temperature))
        self.emoji_label.setText(weather)
        self.description_label.setText(description)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    apps = wapp()

    apps.show()

    sys.exit(app.exec())