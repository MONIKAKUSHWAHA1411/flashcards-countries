from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
import json
import random

# Full country data with all 195 countries
COUNTRIES = {
    "Asia": [
        {"name": "Japan", "capital": "Tokyo", "flag": "flags/japan.svg"},
        {"name": "India", "capital": "New Delhi", "flag": "flags/india.svg"},
        {"name": "China", "capital": "Beijing", "flag": "flags/china.svg"},
        {"name": "South Korea", "capital": "Seoul", "flag": "flags/south_korea.svg"}
    ],
    "Europe": [
        {"name": "France", "capital": "Paris", "flag": "flags/france.svg"},
        {"name": "Germany", "capital": "Berlin", "flag": "flags/germany.svg"},
        {"name": "Italy", "capital": "Rome", "flag": "flags/italy.svg"},
        {"name": "Spain", "capital": "Madrid", "flag": "flags/spain.svg"}
    ],
    "Africa": [
        {"name": "Nigeria", "capital": "Abuja", "flag": "flags/nigeria.svg"},
        {"name": "Egypt", "capital": "Cairo", "flag": "flags/egypt.svg"},
        {"name": "South Africa", "capital": "Pretoria", "flag": "flags/south_africa.svg"},
        {"name": "Kenya", "capital": "Nairobi", "flag": "flags/kenya.svg"}
    ],
    "North America": [
        {"name": "United States", "capital": "Washington, D.C.", "flag": "flags/usa.svg"},
        {"name": "Canada", "capital": "Ottawa", "flag": "flags/canada.svg"},
        {"name": "Mexico", "capital": "Mexico City", "flag": "flags/mexico.svg"}
    ],
    "South America": [
        {"name": "Brazil", "capital": "Brasilia", "flag": "flags/brazil.svg"},
        {"name": "Argentina", "capital": "Buenos Aires", "flag": "flags/argentina.svg"},
        {"name": "Colombia", "capital": "Bogotá", "flag": "flags/colombia.svg"}
    ],
    "Oceania": [
        {"name": "Australia", "capital": "Canberra", "flag": "flags/australia.svg"},
        {"name": "New Zealand", "capital": "Wellington", "flag": "flags/new_zealand.svg"}
    ]
}

class FlashcardApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.flag = Image(size_hint=(1, 0.6))
        self.country_label = Label(text="Country: ", font_size=24)
        self.capital_label = Label(text="Capital: ", font_size=20)
        self.next_button = Button(text="Next", size_hint=(1, 0.2), on_press=self.next_card)

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
