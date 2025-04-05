from kivy.app import App
from kivy.lang import Builder

CONVERSION_FACTOR = 1.60934

class MileToKmApp(App):
    """Miles to km converter app"""

    def build(self):
        """Build UI from .kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Convert miles to km"""
        miles = self.get_valid_miles()
        km = miles * CONVERSION_FACTOR
        self.root.ids.output_label.text = str(km)

    def handle_increment(self, delta):
        """Increase/decrease miles value"""
        miles = self.get_valid_miles() + delta
        self.root.ids.input_miles.text = str(int(miles))
        self.handle_calculate()

    def get_valid_miles(self):
        """Get miles or 0"""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0

MileToKmApp().run()
