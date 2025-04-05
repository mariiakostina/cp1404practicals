from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """App with dynamic labels"""

    def __init__(self, **kwargs):
        """Set up name list"""
        super().__init__(**kwargs)
        self.names = {"Mariia", "Vika", "Mike", "Lena"}

    def build(self):
        """Build GUI and layout"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)
        return self.root

DynamicLabelsApp().run()