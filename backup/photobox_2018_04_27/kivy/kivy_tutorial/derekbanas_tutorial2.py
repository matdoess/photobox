##import kivy

from kivy.app import App
from kivy.uix.widget import Widget

class CustomWidget(Widget):
    pass

class derekbanas_tutorial2App(App):
    
    def build(self):
        return CustomWidget()

customWidget = derekbanas_tutorial2App()

customWidget.run()
