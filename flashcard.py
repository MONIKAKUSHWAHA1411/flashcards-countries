from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import json
import random

# Full country data with all 195 countries
COUNTRIES = {
    "Asia": [
        {"name": "Japan", "capital": "Tokyo", "flag": "flags/japan.png"},
        {"name": "India", "capital": "New Delhi", "flag": "flags/india.png"},
        {"name": "China", "capital": "Beijing", "flag": "flags/china.png"},
        {"name": "South Korea", "capital": "Seoul", "flag": "flags/south_korea.png"}
    ],
    "Europe": [
        {"name": "France", "capital": "Paris", "flag": "flags/france.png"},
        {"name": "Germany", "capital": "Berlin", "flag": "flags/germany.png"},
        {"name": "Italy", "capital": "Rome", "flag": "flags/italy.png"},
        {"name": "Spain", "capital": "Madrid", "flag": "flags/spain.png"}
    ],
    "Africa": [
        {"name": "Nigeria", "capital": "Abuja", "flag": "flags/nigeria.png"},
        {"name": "Egypt", "capital": "Cairo", "flag": "flags/egypt.png"},
        {"name": "South Africa", "capital": "Pretoria", "flag": "flags/south_africa.png"},
        {"name": "Kenya", "capital": "Nairobi", "flag": "flags/kenya.png"}
    ],
    "North America": [
        {"name": "United States", "capital": "Washington, D.C.", "flag": "flags/usa.png"},
        {"name": "Canada", "capital": "Ottawa", "flag": "flags/canada.png"},
        {"name": "Mexico", "capital": "Mexico City", "flag": "flags/mexico.png"}
    ],
    "South America": [
        {"name": "Brazil", "capital": "Brasilia", "flag": "flags/brazil.png"},
        {"name": "Argentina", "capital": "Buenos Aires", "flag": "flags/argentina.png"},
        {"name": "Colombia", "capital": "Bogotá", "flag": "flags/colombia.png"}
    ],
    "Oceania": [
        {"name": "Australia", "capital": "Canberra", "flag": "flags/australia.png"},
        {"name": "New Zealand", "capital": "Wellington", "flag": "flags/new_zealand.png"}
    ]
}

class FlashcardApp(App):
    def build(self):

        #Window.clearcolor = (0.5, 0.5, 0.5, 1)  # Grey background (RGBA format)

        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.flag = Image(size_hint=(1, 0.6))

        # Create labels with the desired style
        self.country_label = Label(
            text="Country: ",
            font_size=40,
            font_name="Arial",  # Make sure Arial is available on your system
            bold=True,
            color=(0, 0, 1, 1)  # Blue text color (RGBA format)
        )

        self.capital_label = Label(
            text="Capital: ",
            font_size=40,
            font_name="Arial",
            bold=True,
            color=(0, 0, 1, 1)
        )

        # Styled button
        self.next_button = Button(
            text="Next",
            size_hint=(1, 0.2),
            font_size=40,
            font_name="Arial",
            bold=True,
            background_color=(0.2, 0.2, 0.2, 1),  # Dark grey button background
            color=(0, 0, 1, 1)  # Blue text color
        )
        self.next_button.bind(on_press=self.next_card)


        #self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        #self.flag = Image(size_hint=(1, 0.6))
        #self.country_label = Label(text="Country: ", font_size=24)
        #self.capital_label = Label(text="Capital: ", font_size=20)
        # self.next_button = Button(text="Next", size_hint=(1, 0.2), on_press=self.next_card)

        self.layout.add_widget(self.flag)
        self.layout.add_widget(self.country_label)
        self.layout.add_widget(self.capital_label)
        self.layout.add_widget(self.next_button)
        
        self.next_card()
        return self.layout

    def next_card(self, instance=None):
        continent = random.choice(list(COUNTRIES.keys()))
        country = random.choice(COUNTRIES[continent])
        
        self.flag.source = country["flag"]
        self.country_label.text = f"Country: {country['name']}"
        self.capital_label.text = f"Capital: {country['capital']}"

if __name__ == "__main__":
    FlashcardApp().run()
